from pathlib import Path

import pygame

# Pygame libary initialization
pygame.init()

# Pygame font and mixer initialization
pygame.font.init()
pygame.mixer.init()

# Base directory: this gets the absolute path of the current file, then gets the parent directory
BASE_DIR = Path(__file__).parent

#
# Game settings
#

# Window settings
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Character settings
CHARACTER_WIDTH = 250
CHARACTER_HEIGHT = 333.5

# Character collision box settings
CHARACTER_COLLISSION_BOX_X = 110
CHARACTER_COLLISSION_BOX_Y = 110
CHARACTER_COLLISION_BOX_WIDTH = 110
CHARACTER_COLLISION_BOX_HEIGHT = 207

# Block settings
BLOCK_WIDTH = 70
BLOCK_HEIGHT = 70

# Background settings
BACKGROUND_LOOP_POINT = 2883

# Ground settings
GROUND_HEIGHT = 42

# Maximum frames per second
MAX_FPS = 60

# Gravity
GRAVITY = 980

TEXTURES = {
    "background": pygame.image.load(BASE_DIR / "assets" / "textures" / "background.png"),
    "ground": pygame.image.load(BASE_DIR / "assets" / "textures" / "ground.png"),
    "bunny": pygame.image.load(BASE_DIR / "assets" / "textures" / "bunny.png"),
}

FRAMES = {
    "bunny_run": [
        pygame.Rect(0, 0, 250, 333.5),
        pygame.Rect(250, 0, 250, 333.5),
        pygame.Rect(500, 0, 250, 333.5),
        pygame.Rect(750, 0, 250, 333.5),
        pygame.Rect(0, 333.5, 250, 333.5),
        pygame.Rect(250, 333.5, 250, 333.5),
        pygame.Rect(500, 333.5, 250, 333.5),
        pygame.Rect(750, 333.5, 250, 333.5),
    ],
    "bunny_idle": [
        pygame.Rect(0, 0, 250, 333.5),
    ],
    "bunny_jump": [
        pygame.Rect(750, 0, 250, 333.5),
    ],
}

pygame.mixer.music.load(BASE_DIR / "assets" / "sounds" / "happy_little.mp3")

SOUNDS = {
    "jump": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "jump.ogg"),
    "explosion": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "explosion.wav"),
    "clock": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "clock.wav"),
}

FONTS = {
    "small": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "game_changer.ttf", 8),
    "medium": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "game_changer.ttf", 16),
}
