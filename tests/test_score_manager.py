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

    def test_add_player_point(self):
        """add_player_point()メソッドのテスト"""
        score_manager = ScoreManager()
        score_manager.add_player_point()
        assert score_manager.player_score == 1

    def test_add_cpu_point(self):
        """add_cpu_point()メソッドのテスト"""
        score_manager = ScoreManager()
        score_manager.add_cpu_point()
        assert score_manager.cpu_score == 1

    def test_score_increments_correctly(self):
        """スコアが正しく増加することのテスト"""
        score_manager = ScoreManager()
        score_manager.add_player_point()
        score_manager.add_player_point()
        score_manager.add_cpu_point()
        assert score_manager.player_score == 2
        assert score_manager.cpu_score == 1