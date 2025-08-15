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

    def calculate_bounce_angle(self, ball, paddle):
        """パドル衝突時の反射角度を計算する

        Args:
            ball: Ballオブジェクト
            paddle: Paddleオブジェクト

        Returns:
            tuple: 新しい速度ベクトル (new_vx, new_vy)
        """
        # 衝突位置の相対位置を計算（-1.0〜1.0）
        ball_center_y = ball.y + ball.size / 2
        paddle_center_y = paddle.get_center_y()
        relative_position = (ball_center_y - paddle_center_y) / (paddle.height / 2)
        
        # 相対位置に応じたY速度の計算
        speed = abs(ball.vx)  # 元の速度の大きさ
        max_angle_factor = 0.75  # 最大角度係数
        new_vy = relative_position * speed * max_angle_factor
        
        # X速度の反転
        new_vx = -ball.vx
        
        return new_vx, new_vy

    def handle_paddle_bounce(self, ball, paddle):
        """パドル反射処理を行う

        Args:
            ball: Ballオブジェクト
            paddle: Paddleオブジェクト
        """
        # ボールを加速（5%）
        ball.accelerate()
        
        # 反射角度を計算
        new_vx, new_vy = self.calculate_bounce_angle(ball, paddle)
        
        # 新しい速度ベクトルを設定
        ball.set_velocity(new_vx, new_vy)