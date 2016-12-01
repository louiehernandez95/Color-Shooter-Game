import random
import pygame
import projectile
import player
import surface_manager

class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy2, self).__init__()
        self.display = pygame.display.get_surface()

        enemy_sprite = pygame.image.load("data/images/enemy_frame2.png").convert_alpha()
        self.image = pygame.transform.flip(enemy_sprite, False, False)
        self.rect = pygame.Rect((0, 0), (self.image.get_width(), self.image.get_height()))
        paths = [[1000, -128, -12, 12], [1000, self.display.get_height()+128, -12, -12]]
        self.pos_x=700
        self.pos_y= random.randint(50,500)
        self.velx=-15
        self.is_hit = False
        self.hit_sound = pygame.mixer.Sound("data/sound/hit.wav")
        self.dirty = 1

    def update(self):
        if self.pos_x < 0 - self.rect.width:
            surface_manager.remove(self)

        self.check_if_hit()
        if self.self_hit()==True:
            return True
        if self.is_hit:
            self.pos_y += 10
            if self.pos_y >= self.display.get_height():
                surface_manager.remove(self)
        if not self.is_hit:
            self.pos_x += self.velx


        self.rect.topleft = (self.pos_x, self.pos_y)
        self.dirty = 1

    def self_hit(self):
        collidelist = pygame.sprite.spritecollide(self, surface_manager.surface_list, False)

        for item in collidelist:
            if type(item) is player.Player:
                print 'hit'
                return True

        return False
    def check_if_hit(self):
        if self.is_hit:
            return
        collidelist = pygame.sprite.spritecollide(self, surface_manager.surface_list, False)

        for item in collidelist:
            if type(item) is projectile.Projectile:
                surface_manager.remove(item)
                self.is_hit = True
                self.image = pygame.transform.flip(self.image, False, True)
                self.hit_sound.play()
