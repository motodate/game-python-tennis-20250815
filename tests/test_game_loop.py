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

    def test_handle_events_method_exists(self):
        self.game_loop = GameLoop()
        assert hasattr(self.game_loop, 'handle_events')
        assert callable(getattr(self.game_loop, 'handle_events'))

    @patch('pygame.event.get')
    def test_quit_event_processing(self, mock_get_events):
        quit_event = MagicMock()
        quit_event.type = pygame.QUIT
        mock_get_events.return_value = [quit_event]
        
        self.game_loop = GameLoop()
        self.game_loop.running = True
        self.game_loop.handle_events()
        
        assert self.game_loop.running == False

    def test_running_attribute_exists(self):
        self.game_loop = GameLoop()
        assert hasattr(self.game_loop, 'running')
        assert isinstance(self.game_loop.running, bool)