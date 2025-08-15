import pygame
from src.utils.settings import GameSettings


class CollisionHandler:
    """衝突判定と物理演算を担当するクラス"""
    
    def __init__(self):
        """CollisionHandlerを初期化"""
        pass

    def check_wall_collision(self, ball):
        """壁との衝突判定を行う

        Args:
            ball: Ballオブジェクト

        Returns:
            bool: 衝突している場合True、していない場合False
        """
        # 上壁判定
        if ball.y <= 0:
            return True
        
        # 下壁判定
        if ball.y + ball.size >= GameSettings.WINDOW_HEIGHT:
            return True
        
        return False

    def handle_wall_bounce(self, ball):
        """壁での反射処理を行う

        Args:
            ball: Ballオブジェクト
        """
        # Y方向の速度を反転
        ball.vy = -ball.vy
        
        # 壁にめり込まないよう位置補正
        if ball.y <= 0:
            ball.y = 0
        elif ball.y + ball.size >= GameSettings.WINDOW_HEIGHT:
            ball.y = GameSettings.WINDOW_HEIGHT - ball.size

    def check_paddle_collision(self, ball, paddle):
        """パドルとの衝突判定を行う

        Args:
            ball: Ballオブジェクト
            paddle: Paddleオブジェクト

        Returns:
            bool: 衝突している場合True、していない場合False
        """
        ball_rect = ball.get_rect()
        paddle_rect = paddle.get_rect()
        
        return ball_rect.colliderect(paddle_rect)