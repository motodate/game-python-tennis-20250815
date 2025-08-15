import pytest


def test_pygame_import():
    """pygameがインポート可能であることを確認"""
    try:
        import pygame

        assert True, "pygameが正常にインポートできます"
    except ImportError:
        pytest.fail("pygameがインポートできません")


def test_pygame_version():
    """pygameのバージョンが取得できることを確認"""
    import pygame

    assert hasattr(pygame, "version"), "pygameにversionが存在しません"
    assert pygame.version.ver is not None, "pygameのバージョンが取得できません"
