import pygame
from src.utils.settings import GameSettings


class Ball:
    """ボールクラス - サイズは設定ファイルで定義"""

    def __init__(self, x, y):
        """Ballを初期化する

        Args:
            x (int): X座標
            y (int): Y座標
        """
        self.x = x
        self.y = y
        self.size = GameSettings.BALL_SIZE