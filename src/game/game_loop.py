import pygame
from src.utils.settings import GameSettings


class GameLoop:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(GameSettings.FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def render(self):
        pass
