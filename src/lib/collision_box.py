"""
This file contains the implementation of the class CollisionBox.

Author: Alejandro Mujica (aledrums@gmail.com)
"""

import pygame


class CollisionBox:
    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        self.box = pygame.Rect(x, y, width, height)

    def collides_with(self, other: "CollisionBox") -> bool:
        return self.box.colliderect(other.box)

    def render(self, surface: pygame.Surface) -> None:
        """
        This render method if for debugging purposes. It draws a red rectangle.
        """
        pygame.draw.rect(surface, (255, 0, 0), self.box, 1)
