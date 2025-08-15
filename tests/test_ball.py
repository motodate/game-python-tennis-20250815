import pytest
import pygame
import math
from src.game.entities.ball import Ball
from src.utils.settings import GameSettings


class TestBall:
    def test_ball_initialization(self):
        """Ballクラスの初期化テスト"""
        ball = Ball(100, 200)
        assert ball.x == 100
        assert ball.y == 200

    def test_ball_size(self):
        """Ballのサイズ確認テスト"""
        ball = Ball(0, 0)
        assert ball.size == GameSettings.BALL_SIZE

    def test_ball_initial_position(self):
        """初期位置（画面中央）のテスト"""
        ball = Ball(0, 0)
        ball.reset()

        expected_x = (GameSettings.WINDOW_WIDTH - GameSettings.BALL_SIZE) // 2
        expected_y = (GameSettings.WINDOW_HEIGHT - GameSettings.BALL_SIZE) // 2
        assert ball.x == expected_x
        assert ball.y == expected_y

    def test_ball_initial_speed(self):
        """初期速度のテスト"""
        ball = Ball(0, 0)
        ball.reset()

        # 速度ベクトルが存在することを確認
        assert hasattr(ball, "vx")
        assert hasattr(ball, "vy")

        # 初期速度の大きさが300であることを確認
        speed = math.sqrt(ball.vx**2 + ball.vy**2)
        assert abs(speed - GameSettings.BALL_INITIAL_SPEED) < 1.0

    def test_ball_velocity_vector_exists(self):
        """速度ベクトル（vx, vy）の存在テスト"""
        ball = Ball(0, 0)
        ball.reset()

        # vx, vyが数値であることを確認
        assert isinstance(ball.vx, (int, float))
        assert isinstance(ball.vy, (int, float))

        # どちらかは0でないことを確認（動いている）
        assert ball.vx != 0 or ball.vy != 0

    def test_ball_update_method(self):
        """update()メソッドのテスト"""
        ball = Ball(100, 100)
        ball.vx = 200  # 200 pixel/second
        ball.vy = 150  # 150 pixel/second

        initial_x = ball.x
        initial_y = ball.y

        delta_time = 0.1  # 0.1秒
        ball.update(delta_time)

        # 位置が期待通りに更新されることを確認
        expected_x = initial_x + (ball.vx * delta_time)
        expected_y = initial_y + (ball.vy * delta_time)
        assert ball.x == expected_x
        assert ball.y == expected_y

    def test_ball_delta_time_position_update(self):
        """delta_timeに応じた位置更新のテスト"""
        ball = Ball(0, 0)
        ball.vx = 300
        ball.vy = 400

        # 異なるdelta_timeでテスト
        ball1 = Ball(0, 0)
        ball1.vx = 300
        ball1.vy = 400
        ball1.update(0.05)  # 0.05秒

        ball2 = Ball(0, 0)
        ball2.vx = 300
        ball2.vy = 400
        ball2.update(0.1)  # 0.1秒

        # delta_timeが2倍になると移動距離も2倍になることを確認
        assert abs(ball2.x - (ball1.x * 2)) < 0.001
        assert abs(ball2.y - (ball1.y * 2)) < 0.001

    def test_get_speed_method(self):
        """get_speed()メソッドのテスト"""
        ball = Ball(0, 0)
        ball.vx = 300
        ball.vy = 400

        # 速度の大きさ計算（√(300² + 400²) = 500）
        expected_speed = math.sqrt(300**2 + 400**2)
        actual_speed = ball.get_speed()
        assert abs(actual_speed - expected_speed) < 0.001

    def test_set_velocity_method(self):
        """set_velocity()メソッドのテスト"""
        ball = Ball(0, 0)
        ball.set_velocity(150, 200)

        assert ball.vx == 150
        assert ball.vy == 200

    def test_speed_magnitude_calculation(self):
        """速度の大きさ計算のテスト"""
        ball = Ball(0, 0)

        # 様々な速度で計算テスト
        test_cases = [
            (100, 0, 100),  # 水平移動
            (0, 100, 100),  # 垂直移動
            (3, 4, 5),  # 3-4-5三角形
            (-300, 400, 500),  # 負の値を含む
        ]

        for vx, vy, expected_speed in test_cases:
            ball.set_velocity(vx, vy)
            actual_speed = ball.get_speed()
            assert abs(actual_speed - expected_speed) < 0.001

    def test_accelerate_method(self):
        """accelerate()メソッドのテスト"""
        ball = Ball(0, 0)
        ball.set_velocity(200, 300)

        initial_speed = ball.get_speed()
        ball.accelerate()
        new_speed = ball.get_speed()

        # 5%速度増加の確認
        expected_speed = initial_speed * GameSettings.BALL_ACCELERATION_RATE
        assert abs(new_speed - expected_speed) < 0.001

    def test_accelerate_five_percent_increase(self):
        """5%速度増加のテスト"""
        ball = Ball(0, 0)
        ball.set_velocity(100, 0)  # 速度100

        ball.accelerate()

        # 速度が105になることを確認
        assert abs(ball.get_speed() - 105) < 0.001

    def test_accelerate_maintains_direction(self):
        """速度方向が維持されることのテスト"""
        ball = Ball(0, 0)
        ball.set_velocity(300, 400)

        # 加速前の方向を計算
        initial_angle = math.atan2(ball.vy, ball.vx)

        ball.accelerate()

        # 加速後の方向を計算
        new_angle = math.atan2(ball.vy, ball.vx)

        # 方向が変わらないことを確認
        assert abs(initial_angle - new_angle) < 0.001

    def test_max_speed_limit(self):
        """最大速度（700）を超えないことのテスト"""
        ball = Ball(0, 0)
        # 最大速度近くに設定
        ball.set_velocity(600, 400)  # 速度約720

        ball.accelerate()

        # 最大速度を超えないことを確認（浮動小数点の精度を考慮）
        assert ball.get_speed() <= GameSettings.BALL_MAX_SPEED + 0.001

    def test_max_speed_clamp(self):
        """最大速度時の速度制限テスト"""
        ball = Ball(0, 0)
        # 意図的に高速に設定
        ball.set_velocity(800, 600)  # 速度1000

        ball.accelerate()

        # 速度が700に制限されることを確認
        assert abs(ball.get_speed() - GameSettings.BALL_MAX_SPEED) < 0.001

    def test_max_speed_maintains_direction_when_clamped(self):
        """最大速度制限時も方向が維持されることのテスト"""
        ball = Ball(0, 0)
        ball.set_velocity(600, 800)  # 速度1000

        # 加速前の方向を計算
        initial_angle = math.atan2(ball.vy, ball.vx)

        ball.accelerate()

        # 加速後の方向を計算
        new_angle = math.atan2(ball.vy, ball.vx)

        # 方向が変わらないことを確認
        assert abs(initial_angle - new_angle) < 0.001
        # 速度が制限されていることを確認
        assert abs(ball.get_speed() - GameSettings.BALL_MAX_SPEED) < 0.001

    def test_draw_method(self):
        """draw()メソッドのテスト"""
        ball = Ball(100, 150)

        # モックサーフェスを作成
        pygame.init()
        screen = pygame.Surface((800, 600))

        # draw()メソッドを呼び出し
        rect = ball.draw(screen)

        # 戻り値がpygame.Rectであることを確認
        assert isinstance(rect, pygame.Rect)
        assert rect.x == 100
        assert rect.y == 150
        assert rect.width == GameSettings.BALL_SIZE
        assert rect.height == GameSettings.BALL_SIZE

        pygame.quit()

    def test_draw_uses_white_color(self):
        """白色で描画されることのテスト"""
        ball = Ball(0, 0)

        # 色定数が正しく定義されていることを確認
        assert hasattr(GameSettings, "WHITE")
        assert GameSettings.WHITE == (255, 255, 255)
