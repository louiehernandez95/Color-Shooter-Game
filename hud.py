import time
import pygame
import state
import surface_manager
#defines and manages the heads up display and all its elements
class Hud(state.State):
    timer = None
    player = None
    game = None
    def __init__(self, game, player, timer):
        self.display = pygame.display.get_surface()

        Hud.player = player
        Hud.timer = timer
        Hud.game = game

        self.font_manager = pygame.font.SysFont("comicssansms", 32)
        self.bullet_element = BulletElement(self.font_manager)
        self.bullet_element2 = BulletElement2(self.font_manager)
        self.score_element = ScoreElement(self.font_manager)
        surface_manager.add(self.bullet_element)
        surface_manager.add(self.bullet_element2)
        surface_manager.add(self.score_element)

    def act(self):
        pass

class BulletElement(pygame.sprite.DirtySprite):
    def __init__(self, font_manager):
        super(BulletElement, self).__init__()
        self.font_manager = font_manager
        self.image = self.font_manager.render("SHOTS LEFT: %d" % Hud.player.bullets, True, (255, 255, 255))
        self.rect = pygame.Rect((0, 0), (self.image.get_width(), self.image.get_height()))
        self.dirty = 1

    def update(self):
        self.image =  self.font_manager.render("SHOTS LEFT: %d" % Hud.player.bullets, True, (255, 255, 255))
        self.dirty = 1
class BulletElement2(pygame.sprite.DirtySprite):
    def __init__(self, font_manager):
        super(BulletElement2, self).__init__()
        self.font_manager = font_manager
        self.image = self.font_manager.render("MEGA SHOTS LEFT: %d" % Hud.player.bullets2, True, (255, 255, 255))
        self.rect = pygame.Rect((0, self.image.get_height() -3),
                                (self.image.get_width(), self.image.get_height()))
        self.dirty = 1

    def update(self):
        self.image =  self.font_manager.render("MEGA SHOTS LEFT: %d" % Hud.player.bullets2, True, (255, 255, 255))
        self.dirty = 1
class ScoreElement(pygame.sprite.DirtySprite):
    def __init__(self, font_manager):
        super(ScoreElement, self).__init__()
        self.display = pygame.display.get_surface()
        self.font_manager = font_manager
        self.image = self.font_manager.render("SCORE: %d" % Hud.game.score, True, (255, 255, 255))
        self.rect = pygame.Rect((self.display.get_width()/2 - self.image.get_width()/2, 0), (self.image.get_width(), self.image.get_height()))
        self.dirty = 1


    def update(self):
        self.image =  self.font_manager.render("SCORE: %d" % Hud.game.score, True, (255, 255, 255))
        self.dirty = 1

class ComboElement(pygame.sprite.DirtySprite):
    def __init__(self, bonus):
        super(ComboElement, self).__init__()
        self.remove_existing()
        self.display = pygame.display.get_surface()
        self.font_manager = pygame.font.SysFont("comicssansms", 32)
        self.image = self.font_manager.render("COMBO! %d PT. BONUS" % bonus, True, (255, 255, 255))
        self.rect = pygame.Rect((0 - self.image.get_width(), self.image.get_height()*10), (self.image.get_width(), self.image.get_height()))
        self.pos_x = 0 - self.image.get_width()
        self.pos_y = self.image.get_height()*2
        self.delay = time.clock()
        self.has_shown = False
        self.dirty = 1


    def update(self):

        if self.pos_x < 0 - self.rect.width and self.has_shown:
            surface_manager.remove(self)

        if not self.has_shown and self.pos_x < 0:
            self.pos_x += 12

        if self.pos_x >= 0 - self.rect.width and time.clock() > self.delay + 3:
            self.has_shown = True
            self.pos_x -= 12

        self.rect.topleft = (self.pos_x, self.pos_y)
        self.dirty = 1

    def remove_existing(self):
        for surface in surface_manager.surface_list:
            if type(surface) is ComboElement:
                surface_manager.remove(surface)
                return

def show_combo(bonus):
    surface_manager.add(ComboElement(bonus))
