#!/usr/bin/env python3
"""
テニスゲームのメインエントリーポイント
"""

import sys
import pygame
from src.ui.game_window import GameWindow
from src.game.game_loop import GameLoop


class TennisGame:
    def __init__(self, headless=False):
        self.headless = headless
        if not headless:
            self.game_window = GameWindow()
        self.game_loop = GameLoop()

    def run(self):
        if self.headless:
            print("ヘッドレスモードで実行中...")
            return

        try:
            self.game_loop.running = True
            while self.game_loop.running:
                self.game_loop.handle_events()
                self.game_loop.update()
                self.game_window.clear_screen()
                self.game_loop.render()
                pygame.display.flip()
                self.game_loop.clock.tick(60)
        finally:
            pygame.quit()


def main():
    """メイン関数"""
    # pytestの検出またはコマンドライン引数でheadlessモードを判定
    headless = "--headless" in sys.argv or "pytest" in sys.modules

    print("テニスゲームを開始します...")
    if headless:
        print("ヘッドレスモードが有効です")

    game = TennisGame(headless=headless)
    game.run()


if __name__ == "__main__":
    main()
