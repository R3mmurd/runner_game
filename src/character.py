import pygame

import settings
from src.lib.animation import Animation
from src.lib.collision_box import CollisionBox
from src.stage import Stage

class Character:
    def __init__(self, stage: Stage) -> None:
        self.stage = stage
        self.x = settings.WINDOW_WIDTH // 2 - settings.CHARACTER_WIDTH // 2
        self.y = settings.WINDOW_HEIGHT - settings.GROUND_HEIGHT - settings.CHARACTER_HEIGHT
        self.width = settings.CHARACTER_WIDTH
        self.height = settings.CHARACTER_HEIGHT
                
        self.texture = settings.TEXTURES["bunny"]
        self.animations = {
            "idle": Animation(settings.FRAMES["bunny_idle"]),
            "run": Animation(settings.FRAMES["bunny_run"], 0.1),
            "jump": Animation(settings.FRAMES["bunny_jump"])
        }

        self.current_animation = self.animations["run"]

        self.vy = 0
        self.on_ground = True
        self.active = True

    def start_running(self) -> None:
        self.change_animation("run")

    def set_idle(self) -> None:
        self.change_animation("idle")
    
    def jump(self) -> None:
        if self.on_ground:
            self.vy = -settings.JUMP_TAKEOFF_SPEED
            self.on_ground = False
            self.change_animation("jump")

    def change_animation(self, new_animation: str) -> None:
        anim = self.animations[new_animation]
        if (new_animation == self.current_animation):
            return
        self.current_animation = anim

    def get_collision_box(self) -> CollisionBox:
        return CollisionBox(self.x + settings.CHARACTER_COLLISION_BOX_X, self.y, settings.CHARACTER_COLLISION_BOX_WIDTH, self.height)

    def update(self, dt: float) -> None:
        self.current_animation.update(dt)

        self.y += self.vy * dt
            
        if not self.on_ground:
            self.vy += settings.GRAVITY * dt

            if self.vy > 0 and self.get_collision_box().collides_with(self.stage.get_collision_box()):
                self.on_ground = True
                self.y = settings.WINDOW_HEIGHT - settings.GROUND_HEIGHT - settings.CHARACTER_HEIGHT
                self.vy = 0
                self.change_animation("run")

    def render(self, surface: pygame.Surface) -> None:
        surface.blit(self.texture, (self.x, self.y), self.current_animation.get_current_frame())
        #self.get_collision_box().render(surface)
