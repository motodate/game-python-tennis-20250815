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

    @classmethod
    def create_left_paddle(cls):
        """左パドルを作成する

        Returns:
            Paddle: 左端に配置されたパドル
        """
        x = GameSettings.PADDLE_LEFT_X
        y = (GameSettings.WINDOW_HEIGHT - GameSettings.PADDLE_HEIGHT) // 2
        return cls(x, y)

    @classmethod
    def create_right_paddle(cls):
        """右パドルを作成する

        Returns:
            Paddle: 右端に配置されたパドル
        """
        x = GameSettings.PADDLE_RIGHT_X
        y = (GameSettings.WINDOW_HEIGHT - GameSettings.PADDLE_HEIGHT) // 2
        return cls(x, y)

    def draw(self, screen):
        """パドルを画面に描画する

        Args:
            screen: pygame.Surfaceオブジェクト

        Returns:
            pygame.Rect: 描画されたパドルの矩形
        """
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, GameSettings.WHITE, rect)
        return rect

    def move_up(self, speed, delta_time):
        """パドルを上に移動する

        Args:
            speed (float): 移動速度 (pixel/second)
            delta_time (float): 経過時間 (seconds)
        """
        self.y -= speed * delta_time
        # 上端チェック
        if self.y < 0:
            self.y = 0

    def move_down(self, speed, delta_time):
        """パドルを下に移動する

        Args:
            speed (float): 移動速度 (pixel/second)
            delta_time (float): 経過時間 (seconds)
        """
        self.y += speed * delta_time
        # 下端チェック
        max_y = GameSettings.WINDOW_HEIGHT - self.height
        if self.y > max_y:
            self.y = max_y

    def get_rect(self):
        """衝突判定用のpygame.Rectを取得する

        Returns:
            pygame.Rect: パドルの矩形
        """
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def get_center_y(self):
        """パドルの中央Y座標を取得する

        Returns:
            float: パドルの中央Y座標
        """
        return self.y + self.height // 2
