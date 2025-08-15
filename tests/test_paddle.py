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