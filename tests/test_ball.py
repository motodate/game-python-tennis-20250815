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