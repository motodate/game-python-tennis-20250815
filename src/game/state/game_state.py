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

    def set_state(self, new_state):
        """状態を設定する

        Args:
            new_state (State): 新しい状態
        """
        self.current_state = new_state

    def get_state(self):
        """現在の状態を取得する

        Returns:
            State: 現在の状態
        """
        return self.current_state

    def is_waiting(self):
        """待機状態かどうかを判定する

        Returns:
            bool: 待機状態の場合True、そうでなければFalse
        """
        return self.current_state == State.WAITING

    def is_playing(self):
        """プレイ中状態かどうかを判定する

        Returns:
            bool: プレイ中状態の場合True、そうでなければFalse
        """
        return self.current_state == State.PLAYING

    def is_game_over(self):
        """ゲームオーバー状態かどうかを判定する

        Returns:
            bool: ゲームオーバー状態の場合True、そうでなければFalse
        """
        return self.current_state == State.GAME_OVER