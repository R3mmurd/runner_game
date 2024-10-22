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

# Tick time for the game loop (in seconds) (60 FPS)
TICK_TIME = 0.016666667

# Gravity
GRAVITY = 0.5

TEXTURES = {
    "background": BASE_DIR / "assets" / "textures" "background.png",
    "ground": BASE_DIR / "assets" / "textures" "ground.png",
    "bunny": BASE_DIR / "assets" / "textures" "bunny.png",
}

FRAMES = {
    "bunny": [
        pygame.Rect(0, 0, 250, 333.5),
        pygame.Rect(250, 0, 250, 333.5),
        pygame.Rect(500, 0, 250, 333.5),
        pygame.Rect(750, 0, 250, 333.5),
        pygame.Rect(0, 333.5, 250, 333.5),
        pygame.Rect(250, 333.5, 250, 333.5),
        pygame.Rect(500, 333.5, 250, 333.5),
        pygame.Rect(750, 333.5, 250, 333.5),
    ]
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
