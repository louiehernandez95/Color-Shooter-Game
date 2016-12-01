
import time
import pygame
from pygame.locals import *

import state
import level
import player
import title
import hud
import highscores
import surface_manager
import enemy_2



class Game(state.State):
    score = 0
    streak_counter = 0
    combo_timer = time.clock()
    player


    def __init__(self):

        self.timer = pygame.time.Clock()
        self.display = pygame.display.get_surface()
        self.level_manager = state.StateMachine(self, level.Level())
        self.player = player.Player()
        Game.player = self.player
        self.hud_manager = state.StateMachine(self, hud.Hud(self, self.player, self.timer))
        self.background = pygame.image.load('data/images/background_frame2.png')
        surface_manager.add(self.player)

        self.music2 = pygame.mixer.Sound("data/sound/THEME_SONG.wav")
        self.music2.play(loops=-1)

    def exit(self):
        self.music2.stop()
        Game.score = 0
        Game.streak_counter = 0
    def reason(self):
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            self.level_manager.current_state.exit()
            return title.Title()
        if self.player.pos_y > self.display.get_height() or enemy_2==False:
            print'game over'
            if Game.streak_counter > 1:
                Game.score += 5 * (Game.streak_counter * 2)
            self.level_manager.current_state.exit()
            return highscores.HighScores(Game.score)


    def act(self):
        self.timer.tick(60)
        surface_manager.clear(self.display, self.background)

        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.player.jump()
        else:
            self.player.stop_jumping()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.player.shoot_bullets()

        check_for_combo()
        self.level_manager.update()
        surface_manager.update()
        dirty_rects = surface_manager.draw(self.display)
        pygame.display.update(dirty_rects)

def update_score():
    Game.score += 5
    Game.combo_timer = time.clock()
    Game.streak_counter += 1


def check_for_combo():
    if Game.streak_counter > 1 and time.clock() > Game.combo_timer + 1:
        Game.score += 5 * (Game.streak_counter * 2)
        hud.show_combo(5 * (Game.streak_counter * 2))
        Game.streak_counter = 0
