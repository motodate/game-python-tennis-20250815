import pytest
import pygame
from unittest.mock import Mock, patch, MagicMock
from src.game.input.input_handler import InputHandler


class TestInputHandler:
    def test_input_handler_exists(self):
        handler = InputHandler()
        assert handler is not None
    
    def test_update(self):
        handler = InputHandler()
        with patch('pygame.key.get_pressed') as mock_get_pressed:
            mock_get_pressed.return_value = [False] * 512
            handler.update()
            assert handler.keys is not None
            mock_get_pressed.assert_called_once()
    
    def test_is_key_pressed(self):
        handler = InputHandler()
        handler.key_states = {pygame.K_SPACE: True}
        handler.previous_keys = {pygame.K_SPACE: False}
        assert handler.is_key_pressed(pygame.K_SPACE) == True
        
        handler.previous_keys = {pygame.K_SPACE: True}
        assert handler.is_key_pressed(pygame.K_SPACE) == False
    
    def test_is_key_held(self):
        handler = InputHandler()
        handler.key_states = {pygame.K_SPACE: True}
        assert handler.is_key_held(pygame.K_SPACE) == True
        
        handler.key_states = {pygame.K_SPACE: False}
        assert handler.is_key_held(pygame.K_SPACE) == False
    
    def test_is_move_up(self):
        handler = InputHandler()
        
        handler.key_states = {pygame.K_w: True}
        assert handler.is_move_up() == True
        
        handler.key_states = {pygame.K_UP: True}
        assert handler.is_move_up() == True
        
        handler.key_states = {}
        assert handler.is_move_up() == False
    
    def test_is_move_down(self):
        handler = InputHandler()
        
        handler.key_states = {pygame.K_s: True}
        assert handler.is_move_down() == True
        
        handler.key_states = {pygame.K_DOWN: True}
        assert handler.is_move_down() == True
        
        handler.key_states = {}
        assert handler.is_move_down() == False
    
    def test_is_action_pressed(self):
        handler = InputHandler()
        handler.key_states = {pygame.K_RETURN: True}
        handler.previous_keys = {pygame.K_RETURN: False}
        assert handler.is_action_pressed() == True
        
        handler.previous_keys = {pygame.K_RETURN: True}
        assert handler.is_action_pressed() == False
    
    def test_is_quit_pressed(self):
        handler = InputHandler()
        handler.key_states = {pygame.K_ESCAPE: True}
        handler.previous_keys = {pygame.K_ESCAPE: False}
        assert handler.is_quit_pressed() == True
        
        handler.previous_keys = {pygame.K_ESCAPE: True}
        assert handler.is_quit_pressed() == False
    
    def test_get_player_movement(self):
        handler = InputHandler()
        
        handler.key_states = {pygame.K_w: True}
        assert handler.get_player_movement() == -1
        
        handler.key_states = {pygame.K_s: True}
        assert handler.get_player_movement() == 1
        
        handler.key_states = {}
        assert handler.get_player_movement() == 0
        
        handler.key_states = {pygame.K_w: True, pygame.K_s: True}
        assert handler.get_player_movement() == -1
    
    def test_handle_events(self):
        handler = InputHandler()
        
        quit_event = Mock(type=pygame.QUIT)
        assert handler.handle_events([quit_event]) == True
        
        keydown_event = Mock(type=pygame.KEYDOWN)
        assert handler.handle_events([keydown_event]) == False
        
        keyup_event = Mock(type=pygame.KEYUP)
        assert handler.handle_events([keyup_event]) == False