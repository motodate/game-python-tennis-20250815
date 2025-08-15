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

    def test_handle_wall_bounce_y_velocity_reversed(self):
        """壁での反射でY方向速度が反転されることをテスト"""
        handler = CollisionHandler()
        ball = Ball(100, -5)  # 上壁を超えた位置
        ball.set_velocity(200, -150)  # 上向きの速度
        
        handler.handle_wall_bounce(ball)
        
        assert ball.vx == 200  # X方向は維持
        assert ball.vy == 150  # Y方向は反転

    def test_handle_wall_bounce_x_velocity_maintained(self):
        """壁での反射でX方向速度が維持されることをテスト"""
        handler = CollisionHandler()
        ball = Ball(100, GameSettings.WINDOW_HEIGHT - 5)  # 下壁を超えた位置
        ball.set_velocity(-180, 120)  # 下向きの速度
        
        handler.handle_wall_bounce(ball)
        
        assert ball.vx == -180  # X方向は維持
        assert ball.vy == -120  # Y方向は反転

    def test_check_paddle_collision_overlapping(self):
        """パドルとの矩形重なり判定をテスト（衝突あり）"""
        handler = CollisionHandler()
        ball = Ball(50, 250)  # パドルと重なる位置
        paddle = Paddle.create_left_paddle()  # 左パドル
        
        assert handler.check_paddle_collision(ball, paddle) is True

    def test_check_paddle_collision_not_overlapping(self):
        """パドルとの矩形重なり判定をテスト（衝突なし）"""
        handler = CollisionHandler()
        ball = Ball(400, 300)  # パドルから離れた位置
        paddle = Paddle.create_left_paddle()  # 左パドル
        
        assert handler.check_paddle_collision(ball, paddle) is False