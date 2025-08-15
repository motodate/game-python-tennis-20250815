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

    def test_update_decreases_time(self):
        """update()メソッドでdelta_timeで時間が減少することをテスト"""
        game_timer = GameTimer()
        game_timer.update(5.0)
        assert game_timer.remaining_time == 55.0

    def test_update_with_multiple_deltas(self):
        """複数回updateを呼び出した時の時間減少をテスト"""
        game_timer = GameTimer()
        game_timer.update(10.0)
        game_timer.update(15.0)
        assert game_timer.remaining_time == 35.0

    def test_time_cannot_go_below_zero(self):
        """0未満にならないことをテスト"""
        game_timer = GameTimer()
        game_timer.update(70.0)  # 60秒を超える時間を減算
        assert game_timer.remaining_time == 0