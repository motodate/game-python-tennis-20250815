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

    def get_speed(self):
        """現在の速度の大きさを取得する

        Returns:
            float: 速度の大きさ (√(vx²+vy²))
        """
        return math.sqrt(self.vx**2 + self.vy**2)

    def set_velocity(self, vx, vy):
        """速度ベクトルを設定する

        Args:
            vx (float): X方向の速度
            vy (float): Y方向の速度
        """
        self.vx = vx
        self.vy = vy

    def accelerate(self):
        """ボールを加速する（5%速度増加）"""
        acceleration_rate = GameSettings.BALL_ACCELERATION_RATE
        self.vx *= acceleration_rate
        self.vy *= acceleration_rate

        # 最大速度チェック
        current_speed = self.get_speed()
        max_speed = GameSettings.BALL_MAX_SPEED

        if current_speed > max_speed:
            # 速度を最大速度に制限（方向は維持）
            ratio = max_speed / current_speed
            self.vx *= ratio
            self.vy *= ratio

    def draw(self, screen):
        """ボールを画面に描画する

        Args:
            screen: pygame.Surfaceオブジェクト

        Returns:
            pygame.Rect: 描画されたボールの矩形
        """
        rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(screen, GameSettings.WHITE, rect)
        return rect
