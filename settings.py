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
CHARACTER_HEIGHT = 233
CHARACTER_COLLISSION_BOX_X = 110
CHARACTER_COLLISION_BOX_WIDTH = 110
JUMP_TAKEOFF_SPEED = 1100

# Block settings
BLOCK_WIDTH = 70
BLOCK_HEIGHT = 70
TIME_BETWEEN_BLOCKS = 1.5

# Background settings
BACKGROUND_LOOPING_POINT = 2883
MAIN_SCROLL_X_VELOCITY = -250
MAIN_SCROLL_X_VELOCITY = -125

# Ground settings
GROUND_HEIGHT = 42

# Tick time for the game loop (in seconds) (60 FPS)
MAX_FPS = 60

# Gravity
GRAVITY = 2450

TEXTURES = {
    "background": pygame.image.load(BASE_DIR / "assets" / "textures" / "background.png"),
    "ground": pygame.image.load(BASE_DIR / "assets" / "textures" / "ground.png"),
    "bunny": pygame.image.load(BASE_DIR / "assets" / "textures" / "bunny.png"),
}

FRAMES = {
    "bunny_run": [
        pygame.Rect(0, 85, 250, 233),
        pygame.Rect(250, 85, 250, 233),
        pygame.Rect(500, 85, 250, 233),
        pygame.Rect(750, 85, 250, 233),
        pygame.Rect(0, 346, 250, 233),
        pygame.Rect(250, 346, 250, 233),
        pygame.Rect(500, 346, 250, 233),
        pygame.Rect(750, 346, 250, 233),
    ],
    "bunny_idle": [
        pygame.Rect(0, 85, 250, 233),
    ],
    "bunny_jump": [
        pygame.Rect(750, 346, 250, 233),
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
