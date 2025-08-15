import pytest
import pygame
from src.game.entities.paddle import Paddle
from src.utils.settings import GameSettings


class TestPaddle:
    def test_paddle_initialization(self):
        """Paddleクラスの初期化テスト"""
        paddle = Paddle(100, 200)
        assert paddle.x == 100
        assert paddle.y == 200
    
    def test_paddle_size(self):
        """Paddleのサイズ確認テスト"""
        paddle = Paddle(0, 0)
        assert paddle.width == GameSettings.PADDLE_WIDTH
        assert paddle.height == GameSettings.PADDLE_HEIGHT
    
    def test_left_paddle_initial_position(self):
        """左パドルの初期位置テスト"""
        left_paddle = Paddle.create_left_paddle()
        assert left_paddle.x == GameSettings.PADDLE_LEFT_X
        expected_y = (GameSettings.WINDOW_HEIGHT - GameSettings.PADDLE_HEIGHT) // 2
        assert left_paddle.y == expected_y
    
    def test_right_paddle_initial_position(self):
        """右パドルの初期位置テスト"""
        right_paddle = Paddle.create_right_paddle()
        assert right_paddle.x == GameSettings.PADDLE_RIGHT_X
        expected_y = (GameSettings.WINDOW_HEIGHT - GameSettings.PADDLE_HEIGHT) // 2
        assert right_paddle.y == expected_y
    
    def test_paddle_center_y_position(self):
        """Y座標が画面中央であることのテスト"""
        paddle = Paddle.create_left_paddle()
        expected_center_y = GameSettings.WINDOW_HEIGHT // 2
        actual_center_y = paddle.y + paddle.height // 2
        assert actual_center_y == expected_center_y
    
    def test_draw_method_creates_rect(self):
        """draw()メソッドがpygame.Rectを正しく生成することをテスト"""
        paddle = Paddle(100, 150)
        
        # モックサーフェスを作成
        pygame.init()
        screen = pygame.Surface((800, 600))
        
        # draw()メソッドを呼び出し
        rect = paddle.draw(screen)
        
        # 戻り値がpygame.Rectであることを確認
        assert isinstance(rect, pygame.Rect)
        assert rect.x == 100
        assert rect.y == 150
        assert rect.width == GameSettings.PADDLE_WIDTH
        assert rect.height == GameSettings.PADDLE_HEIGHT
        
        pygame.quit()
    
    def test_draw_uses_white_color(self):
        """描画色が白であることをテスト"""
        paddle = Paddle(0, 0)
        
        # 色定数が正しく定義されていることを確認
        assert hasattr(GameSettings, 'WHITE')
        assert GameSettings.WHITE == (255, 255, 255)
    
    def test_move_up(self):
        """move_up()メソッドのテスト"""
        paddle = Paddle(100, 200)
        initial_y = paddle.y
        
        # 上に移動
        speed = 300  # pixel/second
        delta_time = 0.1  # 0.1秒
        paddle.move_up(speed, delta_time)
        
        # Y座標が上に移動していることを確認
        expected_y = initial_y - (speed * delta_time)
        assert paddle.y == expected_y
    
    def test_move_down(self):
        """move_down()メソッドのテスト"""
        paddle = Paddle(100, 200)
        initial_y = paddle.y
        
        # 下に移動
        speed = 300  # pixel/second
        delta_time = 0.1  # 0.1秒
        paddle.move_down(speed, delta_time)
        
        # Y座標が下に移動していることを確認
        expected_y = initial_y + (speed * delta_time)
        assert paddle.y == expected_y
    
    def test_movement_with_delta_time(self):
        """移動速度がdelta_timeに比例することをテスト"""
        paddle = Paddle(100, 200)
        initial_y = paddle.y
        
        speed = 500  # pixel/second
        
        # 異なるdelta_timeでテスト
        paddle.move_up(speed, 0.02)  # 0.02秒
        first_movement = initial_y - paddle.y
        
        paddle.y = initial_y  # リセット
        paddle.move_up(speed, 0.04)  # 0.04秒
        second_movement = initial_y - paddle.y
        
        # delta_timeが2倍になると移動距離も2倍になることを確認
        assert abs(second_movement - (first_movement * 2)) < 0.001
    
    def test_move_up_boundary_limit(self):
        """上端での移動制限テスト"""
        # 上端近くに配置
        paddle = Paddle(100, 5)
        
        # 大きく上に移動しようとする
        speed = 1000
        delta_time = 1.0
        paddle.move_up(speed, delta_time)
        
        # Y座標が0以下にならないことを確認
        assert paddle.y >= 0
    
    def test_move_down_boundary_limit(self):
        """下端での移動制限テスト"""
        # 下端近くに配置
        max_y = GameSettings.WINDOW_HEIGHT - GameSettings.PADDLE_HEIGHT
        paddle = Paddle(100, max_y - 5)
        
        # 大きく下に移動しようとする
        speed = 1000
        delta_time = 1.0
        paddle.move_down(speed, delta_time)
        
        # Y座標が画面下端を超えないことを確認
        assert paddle.y <= max_y
    
    def test_boundary_clamp_at_exact_limits(self):
        """境界でのclamp処理テスト"""
        # 上端テスト
        paddle = Paddle(100, 0)
        paddle.move_up(100, 0.1)
        assert paddle.y == 0
        
        # 下端テスト
        max_y = GameSettings.WINDOW_HEIGHT - GameSettings.PADDLE_HEIGHT
        paddle = Paddle(100, max_y)
        paddle.move_down(100, 0.1)
        assert paddle.y == max_y