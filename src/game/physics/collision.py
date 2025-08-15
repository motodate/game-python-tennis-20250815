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