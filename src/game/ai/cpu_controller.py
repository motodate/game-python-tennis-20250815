from enum import Enum


class DifficultyLevel(Enum):
    """CPUの難易度レベル"""
    EASY = "easy"
    NORMAL = "normal"
    HARD = "hard"


class CPUController:
    """CPUが操作するパドルのAIロジック"""
    
    def __init__(self, paddle):
        """CPUControllerを初期化する
        
        Args:
            paddle: 操作するPaddleオブジェクト
        """
        self.paddle = paddle
        self.speed_factor = 0.85  # ボール速度に対する係数
        self.min_speed = 100      # 最小移動速度
        self.dead_zone = 5        # デッドゾーン（ピクセル）
        
    def calculate_target_y(self, ball):
        """ボールの中心Y座標を目標位置として計算する
        
        Args:
            ball: Ballオブジェクト
            
        Returns:
            float: ボールの中心Y座標
        """
        return ball.y + ball.size // 2
    
    def get_movement_direction(self, ball):
        """パドルの移動方向を決定する
        
        Args:
            ball: Ballオブジェクト
            
        Returns:
            int: -1(上), 0(停止), 1(下)
        """
        target_y = self.calculate_target_y(ball)
        current_y = self.paddle.get_center_y()
        
        diff = target_y - current_y
        
        if abs(diff) <= self.dead_zone:
            return 0
        elif diff < 0:
            return -1
        else:
            return 1
    
    def calculate_max_speed(self, ball):
        """CPUパドルの最大移動速度を計算する
        
        Args:
            ball: Ballオブジェクト
            
        Returns:
            float: 最大移動速度
        """
        base_speed = abs(ball.vy) * self.speed_factor
        return max(base_speed, self.min_speed)
    
    def update(self, ball, delta_time):
        """CPUパドルの位置を更新する
        
        Args:
            ball: Ballオブジェクト
            delta_time (float): 経過時間（秒）
        """
        direction = self.get_movement_direction(ball)
        max_speed = self.calculate_max_speed(ball)
        
        if direction == -1:
            self.paddle.move_up(max_speed, delta_time)
        elif direction == 1:
            self.paddle.move_down(max_speed, delta_time)
    
    def predict_ball_position(self, ball, time_ahead):
        """将来のボール位置を予測する（オプション機能）
        
        Args:
            ball: Ballオブジェクト
            time_ahead (float): 予測する時間（秒）
            
        Returns:
            float: 予測されるボールのY座標
        """
        predicted_y = self.calculate_target_y(ball) + ball.vy * time_ahead
        
        # 壁反射を考慮
        screen_height = 600  # TODO: GameSettingsから取得するべき
        if predicted_y < 0:
            predicted_y = abs(predicted_y)
        elif predicted_y > screen_height:
            predicted_y = screen_height - (predicted_y - screen_height)
        
        return predicted_y
    
    def set_difficulty(self, level):
        """CPUの難易度を設定する
        
        Args:
            level (DifficultyLevel): 難易度レベル
        """
        if level == DifficultyLevel.EASY:
            self.speed_factor = 0.7
        elif level == DifficultyLevel.NORMAL:
            self.speed_factor = 0.85
        elif level == DifficultyLevel.HARD:
            self.speed_factor = 1.0