import pytest
import pygame
from unittest.mock import patch, MagicMock
from src.ui.game_window import GameWindow


class TestGameWindow:
    def setup_method(self):
        self.game_window = None

    def teardown_method(self):
        if self.game_window:
            pygame.quit()

    @patch('pygame.init')
    @patch('pygame.display.set_mode')
    def test_game_window_initialization(self, mock_set_mode, mock_init):
        mock_screen = MagicMock()
        mock_set_mode.return_value = mock_screen
        
        self.game_window = GameWindow()
        
        mock_init.assert_called_once()
        assert self.game_window is not None

    @patch('pygame.init')
    @patch('pygame.display.set_mode')
    def test_window_size_800x600(self, mock_set_mode, mock_init):
        mock_screen = MagicMock()
        mock_set_mode.return_value = mock_screen
        
        self.game_window = GameWindow()
        
        mock_set_mode.assert_called_once_with((800, 600))