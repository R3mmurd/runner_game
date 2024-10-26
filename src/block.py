import pygame

import settings
from src.lib.collision_box import CollisionBox


class Box:
    def __init__(self, x: float, y: float, width: float, height: float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.texture = settings.TEXTURES["block"]
        self.active = True

    def get_collision_box(self) -> CollisionBox:
        return CollisionBox(self.x, self.y, self.width, self.height)

    def update(self, dt: float) -> None:
        self.x += settings.MAIN_SCROLL_X_VELOCITY * dt

        if self.x + self.width < 0:
            self.active = False

    def render(self, surface: pygame.Surface) -> None:
        surface.blit(self.texture, (self.x, self.y))
