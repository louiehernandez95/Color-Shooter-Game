import pygame

global bgcolor
bgcolor=(0,0,0)

global WIN_RESX
WIN_RESX=700
global WIN_RESY
WIN_RESY=600

surface = pygame.display.get_surface()
screen = pygame.Surface((WIN_RESX,WIN_RESY))
screen.fill(bgcolor)