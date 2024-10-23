import sys

import pygame

import settings
from src.character import Character
from src.stage import Stage


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(settings.WINDOW_SIZE)
        pygame.display.set_caption("Runner Game")
        self.clock = pygame.time.Clock()
        self.running = False

        # Add stage
        self.stage = Stage()
        
        # Add character
        self.character = Character(self.stage)

    def handle_inputs(self, event: pygame.event.Event) -> None:
        if event.key == pygame.K_ESCAPE:
            self.running = False
        elif event.key == pygame.K_SPACE:
            self.character.jump()

    def update(self, dt: float) -> None:
        self.stage.update(dt)
        self.character.update(dt) 

    def render(self) -> None:
        self.screen.fill((0, 0, 0))
        self.stage.render(self.screen)
        self.character.render(self.screen)
        pygame.display.update()

    def run(self) -> None:
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.handle_inputs(event)

            dt = self.clock.tick(settings.MAX_FPS) / 1000.0
            self.update(dt)
            self.render()

        pygame.font.quit()
        pygame.mixer.quit()
        pygame.quit()
