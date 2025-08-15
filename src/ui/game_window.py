import pygame
from src.utils.settings import GameSettings


class GameWindow:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GameSettings.WINDOW_WIDTH, GameSettings.WINDOW_HEIGHT))
        pygame.display.set_caption(GameSettings.WINDOW_TITLE)