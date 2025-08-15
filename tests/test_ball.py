import pytest
import pygame
from src.game.entities.ball import Ball
from src.utils.settings import GameSettings


class TestBall:
    def test_ball_initialization(self):
        """Ballクラスの初期化テスト"""
        ball = Ball(100, 200)
        assert ball.x == 100
        assert ball.y == 200

    def test_ball_size(self):
        """Ballのサイズ（15x15）確認テスト"""
        ball = Ball(0, 0)
        assert ball.size == GameSettings.BALL_SIZE