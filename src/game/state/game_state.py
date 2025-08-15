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
        self.final_score = None

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

    def start_game(self):
        """ゲームを開始する

        状態をPLAYINGに変更し、ゲーム開始時の初期化を行う
        """
        self.current_state = State.PLAYING

    def end_game(self, final_score):
        """ゲームを終了する

        Args:
            final_score (dict): 最終スコア

        状態をGAME_OVERに変更し、最終スコアを保存する
        """
        self.current_state = State.GAME_OVER
        self.final_score = final_score

    def reset(self):
        """ゲーム状態をリセットする

        状態をWAITINGに変更し、スコアやタイマーをリセットする
        """
        self.current_state = State.WAITING
        self.final_score = None

    def get_message(self):
        """現在の状態に応じたメッセージを取得する

        Returns:
            str|None: 状態に応じたメッセージ、PLAYINGの場合はNone
        """
        if self.current_state == State.WAITING:
            return "Press Enter to Start"
        elif self.current_state == State.GAME_OVER:
            return "Game Over"
        else:  # PLAYING
            return None