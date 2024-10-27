import sys

import pygame

import settings


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(settings.WINDOW_SIZE)
        pygame.display.set_caption("Runner Game")
        self.clock = pygame.time.Clock()
        self.running = False

        # Add stage
        
        # Add character

    def handle_inputs(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update(self) -> None:
        dt = self.clock.tick(settings.MAX_FPS) / 1000.0

    def render(self) -> None:
        pass

    def run(self) -> None:
        self.running = True

        while self.running:
            self.handle_inputs()
            self.update()
            self.render()

        pygame.font.quit()
        pygame.mixer.quit()
        pygame.quit()
