import pytest
from src.game.managers.score_manager import ScoreManager


class TestScoreManager:
    def test_score_manager_exists(self):
        """ScoreManagerクラスが存在することをテスト"""
        score_manager = ScoreManager()
        assert score_manager is not None

    def test_initial_score_is_zero(self):
        """初期スコアが0-0であることをテスト"""
        score_manager = ScoreManager()
        assert score_manager.player_score == 0
        assert score_manager.cpu_score == 0