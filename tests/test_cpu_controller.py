import pytest
from unittest.mock import Mock
from src.game.ai.cpu_controller import CPUController, DifficultyLevel


class TestCPUController:
    """CPUControllerクラスのテスト"""

    def test_cpu_controller_exists(self):
        """CPUControllerクラスが存在することをテスト"""
        # パドルのモックを作成
        mock_paddle = Mock()
        
        # CPUControllerのインスタンスを作成
        cpu_controller = CPUController(mock_paddle)
        
        # CPUControllerが正常に作成されることを確認
        assert cpu_controller is not None
        assert cpu_controller.paddle == mock_paddle

    def test_calculate_target_y(self):
        """calculate_target_yメソッドのテスト"""
        mock_paddle = Mock()
        controller = CPUController(mock_paddle)
        
        # ボールのモックを作成
        mock_ball = Mock()
        mock_ball.y = 300
        mock_ball.size = 20
        
        # ボールの中心Y座標を返すことを確認
        target_y = controller.calculate_target_y(mock_ball)
        expected_y = 300 + 20 // 2  # y + size//2
        assert target_y == expected_y

    def test_get_movement_direction_up(self):
        """ボールが上にある時に-1を返すテスト"""
        mock_paddle = Mock()
        mock_paddle.get_center_y.return_value = 300
        controller = CPUController(mock_paddle)
        
        mock_ball = Mock()
        mock_ball.y = 180  # ボールが上
        mock_ball.size = 20
        
        direction = controller.get_movement_direction(mock_ball)
        assert direction == -1

    def test_get_movement_direction_down(self):
        """ボールが下にある時に1を返すテスト"""
        mock_paddle = Mock()
        mock_paddle.get_center_y.return_value = 300
        controller = CPUController(mock_paddle)
        
        mock_ball = Mock()
        mock_ball.y = 420  # ボールが下
        mock_ball.size = 20
        
        direction = controller.get_movement_direction(mock_ball)
        assert direction == 1

    def test_get_movement_direction_dead_zone(self):
        """デッドゾーン内で0を返すテスト"""
        mock_paddle = Mock()
        mock_paddle.get_center_y.return_value = 300
        controller = CPUController(mock_paddle)
        
        mock_ball = Mock()
        mock_ball.y = 295  # デッドゾーン内
        mock_ball.size = 20
        
        direction = controller.get_movement_direction(mock_ball)
        assert direction == 0

    def test_calculate_max_speed_normal(self):
        """ボールY速度の85%を返すテスト"""
        mock_paddle = Mock()
        controller = CPUController(mock_paddle)
        
        mock_ball = Mock()
        mock_ball.vy = 200
        
        max_speed = controller.calculate_max_speed(mock_ball)
        assert max_speed == 170  # 200 * 0.85

    def test_calculate_max_speed_minimum(self):
        """最小速度保証のテスト"""
        mock_paddle = Mock()
        controller = CPUController(mock_paddle)
        
        mock_ball = Mock()
        mock_ball.vy = 50  # 低速のボール
        
        max_speed = controller.calculate_max_speed(mock_ball)
        assert max_speed == 100  # 最小速度

    def test_update_move_up(self):
        """パドルが上に移動するテスト"""
        mock_paddle = Mock()
        mock_paddle.get_center_y.return_value = 300
        mock_paddle.move_up = Mock()
        controller = CPUController(mock_paddle)
        
        mock_ball = Mock()
        mock_ball.y = 180
        mock_ball.size = 20
        mock_ball.vy = 200
        
        controller.update(mock_ball, 0.016)
        mock_paddle.move_up.assert_called_once_with(170, 0.016)

    def test_update_move_down(self):
        """パドルが下に移動するテスト"""
        mock_paddle = Mock()
        mock_paddle.get_center_y.return_value = 300
        mock_paddle.move_down = Mock()
        controller = CPUController(mock_paddle)
        
        mock_ball = Mock()
        mock_ball.y = 420
        mock_ball.size = 20
        mock_ball.vy = 200
        
        controller.update(mock_ball, 0.016)
        mock_paddle.move_down.assert_called_once_with(170, 0.016)

    def test_update_no_movement(self):
        """デッドゾーン内で移動しないテスト"""
        mock_paddle = Mock()
        mock_paddle.get_center_y.return_value = 300
        mock_paddle.move_up = Mock()
        mock_paddle.move_down = Mock()
        controller = CPUController(mock_paddle)
        
        mock_ball = Mock()
        mock_ball.y = 295
        mock_ball.size = 20
        mock_ball.vy = 200
        
        controller.update(mock_ball, 0.016)
        mock_paddle.move_up.assert_not_called()
        mock_paddle.move_down.assert_not_called()

    def test_set_difficulty_easy(self):
        """EASY難易度のテスト"""
        mock_paddle = Mock()
        controller = CPUController(mock_paddle)
        
        controller.set_difficulty(DifficultyLevel.EASY)
        assert controller.speed_factor == 0.7

    def test_set_difficulty_normal(self):
        """NORMAL難易度のテスト"""
        mock_paddle = Mock()
        controller = CPUController(mock_paddle)
        
        controller.set_difficulty(DifficultyLevel.NORMAL)
        assert controller.speed_factor == 0.85

    def test_set_difficulty_hard(self):
        """HARD難易度のテスト"""
        mock_paddle = Mock()
        controller = CPUController(mock_paddle)
        
        controller.set_difficulty(DifficultyLevel.HARD)
        assert controller.speed_factor == 1.0