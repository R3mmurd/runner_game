"""
This file contains the implementation of a function to render text

Author: Alejandro Mujica (aledrums@gmail.com)
"""

from typing import Optional

import pygame


def render_text(
    surface: pygame.Surface,
    text: str,
    font: pygame.font.Font,
    x: float,
    y: float,
    color: pygame.Color,
    bg_color: Optional[pygame.Color] = None,
    center: bool = False,
    shadowed: bool = False,
):
    text_obj = font.render(text, True, color, bg_color)
    text_rect = text_obj.get_rect()

    if center:
        text_rect.center = (x, y)
    else:
        text_rect.x = x
        text_rect.y = y

    if shadowed:
        shadow_text = font.render(text, True, (0, 0, 0))
        shadow_rect = shadow_text.get_rect()
        shadow_rect.x = text_rect.x + 1
        shadow_rect.y = text_rect.y + 1
        surface.blit(shadow_text, shadow_rect)

    surface.blit(text_obj, text_rect)
