import pytest
from src.game.managers.game_timer import GameTimer


class TestGameTimer:
    def test_game_timer_exists(self):
        """GameTimerクラスが存在することをテスト"""
        game_timer = GameTimer()
        assert game_timer is not None

    def test_initial_time_is_60_seconds(self):
        """初期時間が60秒であることをテスト"""
        game_timer = GameTimer()
        assert game_timer.remaining_time == 60