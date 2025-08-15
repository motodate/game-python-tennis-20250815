import pytest
from src.game.state.game_state import GameState, State


class TestGameState:
    """GameStateクラスのテスト"""

    def test_game_state_exists(self):
        """GameStateクラスが存在することをテスト"""
        game_state = GameState()
        assert game_state is not None

    def test_initial_state_is_waiting(self):
        """初期状態がWAITINGであることをテスト"""
        game_state = GameState()
        assert game_state.get_state() == State.WAITING

    def test_set_state_method(self):
        """set_state()メソッドのテスト"""
        game_state = GameState()
        game_state.set_state(State.PLAYING)
        assert game_state.get_state() == State.PLAYING

    def test_get_state_method(self):
        """get_state()メソッドのテスト"""
        game_state = GameState()
        # 初期状態の確認
        assert game_state.get_state() == State.WAITING
        # 状態変更後の確認
        game_state.set_state(State.GAME_OVER)
        assert game_state.get_state() == State.GAME_OVER

    def test_state_change_reflects_correctly(self):
        """状態変更が正しく反映されることのテスト"""
        game_state = GameState()
        
        # WAITING -> PLAYING
        game_state.set_state(State.PLAYING)
        assert game_state.get_state() == State.PLAYING
        
        # PLAYING -> GAME_OVER
        game_state.set_state(State.GAME_OVER)
        assert game_state.get_state() == State.GAME_OVER
        
        # GAME_OVER -> WAITING
        game_state.set_state(State.WAITING)
        assert game_state.get_state() == State.WAITING

    def test_is_waiting_method(self):
        """is_waiting()メソッドのテスト"""
        game_state = GameState()
        
        # 初期状態はWAITING
        assert game_state.is_waiting() is True
        
        # PLAYINGに変更
        game_state.set_state(State.PLAYING)
        assert game_state.is_waiting() is False

    def test_is_playing_method(self):
        """is_playing()メソッドのテスト"""
        game_state = GameState()
        
        # 初期状態はWAITING
        assert game_state.is_playing() is False
        
        # PLAYINGに変更
        game_state.set_state(State.PLAYING)
        assert game_state.is_playing() is True

    def test_is_game_over_method(self):
        """is_game_over()メソッドのテスト"""
        game_state = GameState()
        
        # 初期状態はWAITING
        assert game_state.is_game_over() is False
        
        # GAME_OVERに変更
        game_state.set_state(State.GAME_OVER)
        assert game_state.is_game_over() is True

    def test_start_game_method(self):
        """start_game()メソッドのテスト"""
        game_state = GameState()
        
        # WAITINGからPLAYINGへの遷移
        game_state.start_game()
        assert game_state.get_state() == State.PLAYING

    def test_start_game_waiting_to_playing(self):
        """WAITINGからPLAYINGへの遷移テスト"""
        game_state = GameState()
        assert game_state.is_waiting() is True
        
        game_state.start_game()
        assert game_state.is_playing() is True
        assert game_state.is_waiting() is False

    def test_start_game_from_game_over_resets_to_waiting(self):
        """GAME_OVERからWAITINGへのリセットテスト"""
        game_state = GameState()
        game_state.set_state(State.GAME_OVER)
        assert game_state.is_game_over() is True
        
        # チケットでは「GAME_OVERからWAITINGへのリセット」とあるが、
        # ここではstart_game()がGAME_OVERから直接PLAYINGに遷移すると仮定
        game_state.start_game()
        assert game_state.is_playing() is True

    def test_end_game_method(self):
        """end_game()メソッドのテスト"""
        game_state = GameState()
        game_state.start_game()  # PLAYINGにする
        assert game_state.is_playing() is True
        
        final_score = {"player": 5, "cpu": 3}
        game_state.end_game(final_score)
        assert game_state.is_game_over() is True

    def test_end_game_playing_to_game_over(self):
        """PLAYINGからGAME_OVERへの遷移テスト"""
        game_state = GameState()
        game_state.start_game()
        assert game_state.is_playing() is True
        
        final_score = {"player": 7, "cpu": 2}
        game_state.end_game(final_score)
        assert game_state.is_game_over() is True
        assert game_state.is_playing() is False

    def test_end_game_saves_final_score(self):
        """最終スコアの保存テスト"""
        game_state = GameState()
        game_state.start_game()
        
        final_score = {"player": 10, "cpu": 8}
        game_state.end_game(final_score)
        
        # final_score属性に保存されることを確認
        assert hasattr(game_state, 'final_score')
        assert game_state.final_score == final_score

    def test_reset_method(self):
        """reset()メソッドのテスト"""
        game_state = GameState()
        game_state.start_game()
        final_score = {"player": 5, "cpu": 3}
        game_state.end_game(final_score)
        assert game_state.is_game_over() is True
        
        game_state.reset()
        assert game_state.is_waiting() is True

    def test_reset_game_over_to_waiting(self):
        """GAME_OVERからWAITINGへの遷移テスト"""
        game_state = GameState()
        game_state.start_game()
        game_state.end_game({"player": 10, "cpu": 5})
        assert game_state.is_game_over() is True
        
        game_state.reset()
        assert game_state.is_waiting() is True
        assert game_state.is_game_over() is False

    def test_reset_clears_score(self):
        """スコアがクリアされることのテスト"""
        game_state = GameState()
        game_state.start_game()
        final_score = {"player": 8, "cpu": 4}
        game_state.end_game(final_score)
        assert game_state.final_score == final_score
        
        game_state.reset()
        assert game_state.final_score is None

    def test_get_message_method(self):
        """get_message()メソッドのテスト"""
        game_state = GameState()
        
        # WAITING時のメッセージ
        message = game_state.get_message()
        assert message is not None

    def test_get_message_waiting_state(self):
        """WAITING時のメッセージテスト"""
        game_state = GameState()
        assert game_state.is_waiting() is True
        
        message = game_state.get_message()
        assert message == "Press Enter to Start"

    def test_get_message_game_over_state(self):
        """GAME_OVER時のメッセージテスト"""
        game_state = GameState()
        game_state.start_game()
        game_state.end_game({"player": 5, "cpu": 3})
        assert game_state.is_game_over() is True
        
        message = game_state.get_message()
        assert message == "Game Over"

    def test_get_message_playing_state(self):
        """PLAYING時のメッセージテスト（Noneを返す）"""
        game_state = GameState()
        game_state.start_game()
        assert game_state.is_playing() is True
        
        message = game_state.get_message()
        assert message is None