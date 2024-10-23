import pygame

import settings
from src.lib.collision_box import CollisionBox

class Stage:
    def __init__(self) -> None:
        self.background = settings.TEXTURES["background"]
        self.ground = settings.TEXTURES["ground"]
        self.background_x = 0
        self.ground_x = 0
        pygame.mixer.music.play(-1)

    def get_collision_box(self) -> CollisionBox:
        return CollisionBox(0, settings.WINDOW_HEIGHT - settings.GROUND_HEIGHT, settings.WINDOW_WIDTH, settings.GROUND_HEIGHT)

    def update(self, dt: float) -> None:
        self.background_x += settings.BACK_SCROLL_SPEED * dt

        if self.background_x <= -settings.BACKGROUND_LOOPING_POINT:
            self.background_x = 0

        self.ground_x += settings.MAIN_SCROLL_SPEED * dt

        if self.ground_x <= -settings.WINDOW_WIDTH:
            self.ground_x = 0

    def render(self, surface: pygame.Surface) -> None:
        surface.blit(self.background, (self.background_x, 0))
        surface.blit(self.ground, (self.ground_x, settings.WINDOW_HEIGHT - settings.GROUND_HEIGHT))
        #self.get_collision_box().render(surface)
