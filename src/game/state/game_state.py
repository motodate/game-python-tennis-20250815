from enum import Enum


class State(Enum):
    """ゲーム状態の列挙型"""
    WAITING = "waiting"
    PLAYING = "playing"
    GAME_OVER = "game_over"


class GameState:
    """ゲーム状態管理クラス"""
    
    def __init__(self):
        """GameStateを初期化"""
        self.current_state = State.WAITING

    def get_state(self):
        """現在の状態を取得する

        Returns:
            State: 現在の状態
        """
        return self.current_state