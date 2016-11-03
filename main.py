import pygame

import state
import title


pygame.init()
display = pygame.display.set_mode((700,600))
pygame.display.set_caption("Planet Parenthood")

class Planet_Parenthood():
    def __init__(self):
        self.sm = state.StateMachine(self, title.Title())

    def start(self):
        while True:
            self.sm.update()

if __name__ == "__main__":
    game = Planet_Parenthood()
    game.start()