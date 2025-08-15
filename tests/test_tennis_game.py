import pytest
import pygame
from unittest.mock import Mock, patch
from src.game.tennis_game import TennisGame


class TestTennisGame:
    def test_tennis_game_exists(self):
        """TennisGameクラスが存在することを確認"""
        assert TennisGame is not None
    
    def test_tennis_game_init(self):
        """TennisGameクラスが正常に初期化されることを確認"""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'):
            game = TennisGame()
            assert game is not None
    
    def test_initialize_components(self):
        """initialize_componentsメソッドのテスト"""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'):
            game = TennisGame()
            game.initialize_components()
            
            # 各コンポーネントが初期化されていることを確認
            assert game.window is not None
            assert game.player_paddle is not None
            assert game.cpu_paddle is not None
            assert game.ball is not None
            assert game.score_manager is not None
            assert game.game_timer is not None
            assert game.game_state is not None
            assert game.input_handler is not None
            assert game.cpu_controller is not None
            assert game.collision_handler is not None
            assert game.clock is not None
            assert game.font is not None
    
    def test_update(self):
        """updateメソッドのテスト"""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'), \
             patch('pygame.key.get_pressed', return_value={}), \
             patch('pygame.event.get', return_value=[]):
            game = TennisGame()
            game.initialize_components()
            
            # delta_timeで更新処理をテスト
            delta_time = 0.016  # 約60fps
            game.update(delta_time)
            
            # 更新処理が呼ばれることを確認（例外が出ないことで確認）
            assert True  # 例外が出なければ成功
    
    def test_update_playing(self):
        """update_playingメソッドのテスト"""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'), \
             patch('pygame.key.get_pressed', return_value={}), \
             patch('pygame.event.get', return_value=[]):
            game = TennisGame()
            game.initialize_components()
            
            # プレイ中状態に設定
            game.game_state.start_game()
            
            # delta_timeでプレイ中更新処理をテスト
            delta_time = 0.016  # 約60fps
            game.update_playing(delta_time)
            
            # プレイ中更新処理が呼ばれることを確認（例外が出ないことで確認）
            assert True  # 例外が出なければ成功
    
    def test_render(self):
        """renderメソッドのテスト"""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'), \
             patch('pygame.display.flip'), \
             patch('pygame.draw.rect'), \
             patch('pygame.draw.line'):
            game = TennisGame()
            game.initialize_components()
            
            # 描画処理をテスト
            game.render()
            
            # 描画処理が呼ばれることを確認（例外が出ないことで確認）
            assert True  # 例外が出なければ成功
    
    def test_draw_text(self):
        """draw_textメソッドのテスト"""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font') as mock_font:
            
            # モックフォントの設定
            mock_font_instance = Mock()
            mock_font.return_value = mock_font_instance
            mock_surface = Mock()
            mock_font_instance.render.return_value = mock_surface
            mock_surface.get_rect.return_value = pygame.Rect(0, 0, 100, 30)
            
            game = TennisGame()
            game.initialize_components()
            
            # テキスト描画をテスト
            game.draw_text("Test Text", 100, 200)
            
            # テキスト描画処理が呼ばれることを確認（例外が出ないことで確認）
            assert True  # 例外が出なければ成功
    
    def test_run(self):
        """runメソッドのテスト（終了条件のテスト）"""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'), \
             patch('pygame.key.get_pressed', return_value={}), \
             patch('pygame.event.get') as mock_events, \
             patch('pygame.display.flip'), \
             patch('pygame.draw.rect'), \
             patch('pygame.draw.line'):
            
            # QUITイベントを含むイベントリストを設定
            quit_event = Mock()
            quit_event.type = pygame.QUIT
            mock_events.return_value = [quit_event]
            
            game = TennisGame()
            game.initialize_components()
            
            # runメソッドをテスト（QUITイベントで終了するはず）
            game.run()
            
            # 正常にrunメソッドが終了することを確認
            assert True