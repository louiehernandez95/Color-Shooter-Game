import pygame
import random
import projectile
import player
import surface_manager
import game
#second enemy type class
#similar functionality as enemy_1
class Enemy2(pygame.sprite.DirtySprite):
    def __init__(self, img):
        super(Enemy2, self).__init__()
        self.display = pygame.display.get_surface()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = pygame.Rect((0, 0), (self.image.get_width(), self.image.get_height()))
        self.pos_x = self.display.get_width()
        self.pos_y = random.randint(50,500)
        self.velx=-15
        self.hit_sound = pygame.mixer.Sound("data/sound/hit.wav")
        self.dirty = 1
        self.is_hit=False
    def self_hit(self):
        collidelist = pygame.sprite.spritecollide(self, surface_manager.surface_list, False)
        for item in collidelist:
            if type(item) is player.Player:
                surface_manager.remove(self)
                if game.Game.player.bullets<=0:
                    return;
                game.Game.player.bullets-=5



class Enemy_enter(Enemy2):
    def __init__(self):
        super(Enemy_enter, self).__init__("data/images/enemy_frame2.png")

    def update(self):
        if self.pos_x < 0 - self.rect.width:
            surface_manager.remove(self)

        self.check_if_hit()
        self.check_if_hit2()
        self.self_hit()
        if self.is_hit:
            self.pos_y += 10
            if self.pos_y >= self.display.get_height():
                surface_manager.remove(self)
        if not self.is_hit:
            self.pos_x += self.velx


        self.rect.topleft = (self.pos_x, self.pos_y)
        self.dirty = 1
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
    def check_if_hit2(self):
        if self.is_hit:
            return
        collidelist = pygame.sprite.spritecollide(self, surface_manager.surface_list, False)

        for item in collidelist:
            if type(item) is projectile.Projectile2:
                self.is_hit = True
                self.image = pygame.transform.flip(self.image, False, True)
                self.hit_sound.play()
