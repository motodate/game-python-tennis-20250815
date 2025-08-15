import pytest
import pygame
from unittest.mock import patch, MagicMock
from src.ui.game_window import GameWindow
from src.game.game_loop import GameLoop


class TestWindowIntegration:
    def setup_method(self):
        self.game_window = None
        self.game_loop = None

    def teardown_method(self):
        if self.game_window or self.game_loop:
            pygame.quit()

    @patch('pygame.init')
    @patch('pygame.display.set_mode')
    @patch('pygame.time.Clock')
    def test_game_window_and_loop_integration(self, mock_clock, mock_set_mode, mock_init):
        mock_screen = MagicMock()
        mock_set_mode.return_value = mock_screen
        mock_clock_instance = MagicMock()
        mock_clock.return_value = mock_clock_instance
        
        self.game_window = GameWindow()
        self.game_loop = GameLoop()
        
        assert self.game_window is not None
        assert self.game_loop is not None
        mock_init.assert_called()

    @patch('pygame.init')
    @patch('pygame.display.set_mode')
    def test_window_clear_screen_integration(self, mock_set_mode, mock_init):
        mock_screen = MagicMock()
        mock_set_mode.return_value = mock_screen
        
        self.game_window = GameWindow()
        self.game_window.clear_screen()
        
        mock_screen.fill.assert_called_once_with((0, 0, 0))

    @patch('pygame.event.get')
    @patch('pygame.time.Clock')
    def test_game_loop_quit_integration(self, mock_clock, mock_get_events):
        quit_event = MagicMock()
        quit_event.type = pygame.QUIT
        mock_get_events.return_value = [quit_event]
        mock_clock_instance = MagicMock()
        mock_clock.return_value = mock_clock_instance
        
        self.game_loop = GameLoop()
        self.game_loop.running = True
        self.game_loop.handle_events()
        
        assert self.game_loop.running == False