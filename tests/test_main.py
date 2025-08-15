import os
import pytest
import subprocess
import sys


def test_main_py_exists():
    """main.pyが存在することを確認"""
    assert os.path.exists("main.py"), "main.pyが存在しません"


def test_main_py_is_executable():
    """main.pyがヘッドレスモードで実行可能であることを確認"""
    result = subprocess.run(
        [sys.executable, "main.py", "--headless"],
        capture_output=True,
        text=True,
        timeout=5,
    )
    # main.pyが存在し、構文エラーがないことを確認
    # ヘッドレスモードでは即座に終了する
    assert result.returncode == 0, f"main.pyの実行に失敗しました: {result.stderr}"
    assert "テニスゲームを開始します..." in result.stdout
    assert "ヘッドレスモードが有効です" in result.stdout


def test_main_py_has_main_block():
    """main.pyにif __name__ == "__main__":ブロックが存在することを確認"""
    with open("main.py", "r", encoding="utf-8") as f:
        content = f.read()
    assert (
        'if __name__ == "__main__":' in content
    ), "main.pyにif __name__ == '__main__':ブロックが存在しません"
