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