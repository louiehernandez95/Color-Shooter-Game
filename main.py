import pygame

import state
import title
from background import TestSprite
#sets display and onscreen images/states like title
pygame.init()
display = pygame.display.set_mode((700,600))
pygame.display.set_caption("Color Shooter")
my_sprite = TestSprite()
my_group = pygame.sprite.Group(my_sprite)

class Color_Shooter():
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
    game = Color_Shooter()
    game.start()
