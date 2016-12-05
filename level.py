import pygame
import random
import time
import state
import platform
import enemy
import powerup
import surface_manager
import enemy_2

class Level(state.State):
    surface_manager = pygame.sprite.RenderUpdates()
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.current_platforms = []
        self.num_of_platforms = 4
        self.background = pygame.image.load('data/images/background_frame2.png')

        self.display.blit(self.background, (0, 0))
        self.enter()

    def enter(self):
        new_platform = platform.StartingPlatform("data/images/platform.png")
        surface_manager.add(new_platform)
        self.current_platforms.append(new_platform)
        self.time_since_last_powerup = time.clock()
        self.time_since_last_powerup2 = time.clock()
        self.time_since_last_enemyspawn = time.clock()
        self.time_since_last_enemyspawn2 = time.clock()
    def exit(self):
        surface_manager.empty()

    def act(self):
        self.check_platforms()

        if (len(self.current_platforms) < self.num_of_platforms) \
                and ((self.current_platforms[-1].pos_x + self.current_platforms[-1].rect.width) <= (self.display.get_width() - random.randint(100, 600))):
            new_platform = platform.Platform("data/images/platform.png")
            surface_manager.add(new_platform)
            self.current_platforms.append(new_platform)
        if time.clock() >= self.time_since_last_powerup + 20:
            surface_manager.add(powerup.BulletPU())
            self.time_since_last_powerup = time.clock()
        if time.clock() >= self.time_since_last_powerup2 + 50:
            surface_manager.add(powerup.BulletPU2())
            self.time_since_last_powerup2 = time.clock()
        if time.clock() >= self.time_since_last_enemyspawn + .5:
            surface_manager.add(enemy.Enemy())
            self.time_since_last_enemyspawn = time.clock()
        if time.clock() >= self.time_since_last_enemyspawn2 + .75:
            surface_manager.add(enemy_2.Enemy_enter())
            self.time_since_last_enemyspawn2 = time.clock()

    def check_platforms(self):
        for platform in self.current_platforms:
            if not surface_manager.has(platform):
                self.current_platforms.remove(platform)