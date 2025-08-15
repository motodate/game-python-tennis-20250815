import pygame
import random
import math
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
        self.vx = 0
        self.vy = 0

    def reset(self):
        """ボールを初期状態にリセットする"""
        # 画面中央に配置
        self.x = (GameSettings.WINDOW_WIDTH - self.size) // 2
        self.y = (GameSettings.WINDOW_HEIGHT - self.size) // 2
        
        # ランダムな方向への速度分配
        angle = random.uniform(0, 2 * math.pi)
        speed = GameSettings.BALL_INITIAL_SPEED
        self.vx = speed * math.cos(angle)
        self.vy = speed * math.sin(angle)

    def update(self, delta_time):
        """ボールの位置を更新する

        Args:
            delta_time (float): 経過時間 (seconds)
        """
        self.x += self.vx * delta_time
        self.y += self.vy * delta_time