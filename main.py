#!/usr/bin/env python3
"""
テニスゲームのメインエントリーポイント
"""

import sys
from src.game.tennis_game import TennisGame


def main():
    """メイン関数"""
    # pytestの検出またはコマンドライン引数でheadlessモードを判定
    headless = "--headless" in sys.argv or "pytest" in sys.modules

    print("テニスゲームを開始します...")
    
    if headless:
        print("ヘッドレスモードが有効です")
        return
    
    game = TennisGame()
    game.initialize_components()
    game.run()


if __name__ == "__main__":
    main()
