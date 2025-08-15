import pytest
import pygame
from unittest.mock import patch, MagicMock
from src.game.game_loop import GameLoop


class TestGameLoop:
    def setup_method(self):
        self.game_loop = None

    def teardown_method(self):
        if self.game_loop:
            pygame.quit()

    def test_game_loop_class_exists(self):
        self.game_loop = GameLoop()
        assert self.game_loop is not None

    def test_run_method_exists(self):
        self.game_loop = GameLoop()
        assert hasattr(self.game_loop, 'run')
        assert callable(getattr(self.game_loop, 'run'))

    def test_fps_setting_60(self):
        from src.utils.settings import GameSettings
        self.game_loop = GameLoop()
        assert GameSettings.FPS == 60

    @patch('pygame.time.Clock')
    def test_clock_initialization(self, mock_clock):
        mock_clock_instance = MagicMock()
        mock_clock.return_value = mock_clock_instance
        
        self.game_loop = GameLoop()
        
        mock_clock.assert_called_once()