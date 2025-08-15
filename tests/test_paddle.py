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
        """Paddleのサイズ（15x100）確認テスト"""
        paddle = Paddle(0, 0)
        assert paddle.width == GameSettings.PADDLE_WIDTH
        assert paddle.height == GameSettings.PADDLE_HEIGHT