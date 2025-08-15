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
        assert hasattr(ball, 'vx')
        assert hasattr(ball, 'vy')
        
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
        ball2.update(0.1)   # 0.1秒
        
        # delta_timeが2倍になると移動距離も2倍になることを確認
        assert abs(ball2.x - (ball1.x * 2)) < 0.001
        assert abs(ball2.y - (ball1.y * 2)) < 0.001