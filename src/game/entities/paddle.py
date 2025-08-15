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