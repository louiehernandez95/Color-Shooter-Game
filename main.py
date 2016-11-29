import pygame

import state
import title
from background import TestSprite

pygame.init()
display = pygame.display.set_mode((700,600))
pygame.display.set_caption("Highway to Hell")
my_sprite = TestSprite()
my_group = pygame.sprite.Group(my_sprite)

class Highway_to_Hell():
    def __init__(self):
        self.sm = state.StateMachine(self, title.Title())

    def start(self):
        x=0
        while True:
            self.sm.update()
            if x%50==0:
                my_group.update()
                my_group.draw(display)
                pygame.display.flip()
            x+=1
if __name__ == "__main__":
    game = Highway_to_Hell()
    game.start()