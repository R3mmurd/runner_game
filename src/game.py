import sys

import pygame

import settings
from src.character import Character
from src.stage import Stage
from src.lib.text import render_text


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

        self.starting = True

        self.score = 0

        self.counter = 3
        self.counter_timer = 0

    def start(self) -> None:
        self.starting = False
        self.character.start_running()

    def reset(self) -> None:
        self.stage.reset()
        self.character.reset()
        self.starting = True
        self.counter = 3
        self.counter_timer = 0
        self.score = 0

    def handle_inputs(self, event: pygame.event.Event) -> None:
        if event.key == pygame.K_ESCAPE:
            self.running = False
        elif not self.starting and event.key == pygame.K_SPACE:
            self.character.jump()

    def update(self, dt: float) -> None:
        if self.starting:
            self.counter_timer += dt
            if self.counter_timer >= 1:
                self.counter_timer = 0
                self.counter -= 1

                if self.counter == 0:
                    self.start()
        else:
            self.stage.update(dt)
            self.character.update(dt)

            for block in self.stage.blocks:
                if self.character.get_collision_box().collides_with(
                    block.get_collision_box()
                ):
                    settings.SOUNDS["explosion"].play()
                    self.reset()
                elif self.character.x > block.x + block.width and not block.scored:
                    self.score += 1
                    block.scored = True

    def render(self) -> None:
        self.screen.fill((0, 0, 0))
        self.stage.render(self.screen)
        self.character.render(self.screen)

        if self.starting:
            render_text(
                self.screen,
                f"{self.counter}",
                settings.FONTS["medium"],
                settings.WINDOW_WIDTH // 2,
                settings.WINDOW_HEIGHT // 2,
                (255, 255, 255),
                center=True,
                shadowed=True,
            )

        render_text(
            self.screen,
            f"Score: {self.score}",
            settings.FONTS["small"],
            settings.WINDOW_WIDTH - 300,
            40,
            (255, 255, 255),
            shadowed=True,
        )

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
