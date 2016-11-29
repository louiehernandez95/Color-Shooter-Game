import pygame
import time

def load_image(name):
    image = pygame.image.load(name)
    return image

class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        self.images.append(load_image('data/images/background_frame1.png'))
        self.images.append(load_image('data/images/background_frame2.png'))
        self.images.append(load_image('data/images/background_frame3.png'))


        self.current_frame = 0
        self.timer = time.clock()

        self.image = self.images[self.current_frame]
        self.rect = pygame.Rect(0, 0, 700, 600)

    def update(self):
        if time.clock() >= self.timer + .5:
            try:
                self.current_frame += 1
                self.image = self.images[self.current_frame]
            except IndexError:
                self.current_frame = 0
                self.image = self.images[self.current_frame]
            self.timer = time.clock()