import pytest
import pygame
from src.game.physics.collision import CollisionHandler
from src.game.entities.ball import Ball
from src.game.entities.paddle import Paddle
from src.utils.settings import GameSettings


class TestCollisionHandler:
    """CollisionHandlerクラスのテスト"""

    def test_collision_handler_exists(self):
        """CollisionHandlerクラスが存在することをテスト"""
        handler = CollisionHandler()
        assert handler is not None