import os
import pytest


def test_src_directory_exists():
    """src/ディレクトリが存在することを確認"""
    assert os.path.exists("src"), "src/ディレクトリが存在しません"


def test_src_game_directory_exists():
    """src/game/ディレクトリが存在することを確認"""
    assert os.path.exists("src/game"), "src/game/ディレクトリが存在しません"


def test_src_ui_directory_exists():
    """src/ui/ディレクトリが存在することを確認"""
    assert os.path.exists("src/ui"), "src/ui/ディレクトリが存在しません"


def test_src_utils_directory_exists():
    """src/utils/ディレクトリが存在することを確認"""
    assert os.path.exists("src/utils"), "src/utils/ディレクトリが存在しません"


def test_tests_directory_exists():
    """tests/ディレクトリが存在することを確認"""
    assert os.path.exists("tests"), "tests/ディレクトリが存在しません"


def test_src_init_py_exists():
    """src/__init__.pyが存在することを確認"""
    assert os.path.exists("src/__init__.py"), "src/__init__.pyが存在しません"


def test_src_game_init_py_exists():
    """src/game/__init__.pyが存在することを確認"""
    assert os.path.exists("src/game/__init__.py"), "src/game/__init__.pyが存在しません"


def test_src_ui_init_py_exists():
    """src/ui/__init__.pyが存在することを確認"""
    assert os.path.exists("src/ui/__init__.py"), "src/ui/__init__.pyが存在しません"


def test_src_utils_init_py_exists():
    """src/utils/__init__.pyが存在することを確認"""
    assert os.path.exists("src/utils/__init__.py"), "src/utils/__init__.pyが存在しません"