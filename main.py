import pygame

import state
import title


pygame.init()
display = pygame.display.set_mode((700,600))
pygame.display.set_caption("Highway to Hell")

class Highway_to_Hell():
    def __init__(self):
        self.sm = state.StateMachine(self, title.Title())

    def start(self):
        while True:
            self.sm.update()

if __name__ == "__main__":
    game = Highway_to_Hell()
    game.start()