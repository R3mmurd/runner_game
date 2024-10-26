import random

import pygame

import settings
from src.lib.collision_box import CollisionBox
from src.block import Block


class Stage:
    def __init__(self) -> None:
        self.background = settings.TEXTURES["background"]
        self.ground = settings.TEXTURES["ground"]
        self.background_x = 0
        self.ground_x = 0
        self.blocks = []
        self.block_timer = 0
        pygame.mixer.music.play(-1)

    def reset(self) -> None:
        self.background_x = 0
        self.ground_x = 0
        self.block_timer = 0
        self.blocks = []

    def get_collision_box(self) -> CollisionBox:
        return CollisionBox(
            0,
            settings.WINDOW_HEIGHT - settings.GROUND_HEIGHT,
            settings.WINDOW_WIDTH,
            settings.GROUND_HEIGHT,
        )

    def update(self, dt: float) -> None:
        self.block_timer += dt
        if self.block_timer >= settings.TIME_BETWEEN_BLOCKS:
            x = settings.WINDOW_WIDTH
            y = (
                settings.WINDOW_HEIGHT
                - settings.GROUND_HEIGHT
                - settings.BLOCK_HEIGHT * random.choice([1, 2.3, 4])
            )
            self.blocks.append(Block(x, y, settings.BLOCK_WIDTH, settings.BLOCK_HEIGHT))
            self.block_timer %= settings.TIME_BETWEEN_BLOCKS

        self.background_x += settings.BACK_SCROLL_X_VELOCITY * dt

        if self.background_x <= -settings.BACKGROUND_LOOPING_POINT:
            self.background_x = 0

        self.ground_x += settings.MAIN_SCROLL_X_VELOCITY * dt

        if self.ground_x <= -settings.WINDOW_WIDTH:
            self.ground_x = 0

        for block in self.blocks:
            block.update(dt)

        self.blocks = [block for block in self.blocks if block.active]

    def render(self, surface: pygame.Surface) -> None:
        surface.blit(self.background, (self.background_x, 0))
        surface.blit(
            self.ground,
            (self.ground_x, settings.WINDOW_HEIGHT - settings.GROUND_HEIGHT),
        )
        # self.get_collision_box().render(surface)
        for block in self.blocks:
            block.render(surface)
