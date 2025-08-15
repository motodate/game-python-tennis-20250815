import pygame
from src.utils.settings import GameSettings


class Paddle:
    """パドルクラス - サイズは設定ファイルで定義"""
    
    def __init__(self, x, y):
        """Paddleを初期化する
        
        Args:
            x (int): X座標
            y (int): Y座標
        """
        self.x = x
        self.y = y
        self.width = GameSettings.PADDLE_WIDTH
        self.height = GameSettings.PADDLE_HEIGHT