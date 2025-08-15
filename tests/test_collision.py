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

    def test_check_wall_collision_top(self):
        """上壁との衝突判定をテスト"""
        handler = CollisionHandler()
        ball = Ball(100, -5)  # 上壁を超えた位置
        assert handler.check_wall_collision(ball) is True

    def test_check_wall_collision_bottom(self):
        """下壁との衝突判定をテスト"""
        handler = CollisionHandler()
        ball = Ball(100, GameSettings.WINDOW_HEIGHT - 5)  # 下壁を超えた位置
        assert handler.check_wall_collision(ball) is True

    def test_check_wall_collision_none(self):
        """壁との衝突がない場合をテスト"""
        handler = CollisionHandler()
        ball = Ball(100, 100)  # 画面内の位置
        assert handler.check_wall_collision(ball) is False