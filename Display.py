import pygame
import time
#Lets Set up our window
pygame.init()
display_width=1000
display_height=600
#RGB colors
black=(0,0,0)
white=(255,255,255)
ship_height= 72
gameDisplay =pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Planet Parenthood") #Changes the title of the window
clock=pygame.time.Clock()

shipIMG= pygame.image.load('ship')
def ship(x,y):
    gameDisplay.blit(shipIMG,(x,y))
def text_objects(text, font):
    textSurface=font.render(text, True,black)
    return textSurface, textSurface.get_rect()
def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect =text_objects(text,largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)

    game_loop()
def crash():
    message_display('You Crashed')
def game_loop():
    x=0
    y=(display_height*0.5)
    y_change=0
    #So the user has to X out in order to exit the window
    gameExit=False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_DOWN:
                    y_change= 5
                elif event.key ==pygame.K_UP:
                    y_change= -5
            if event.type ==pygame.KEYUP:
                if event.key==pygame.K_UP or event.key== pygame.K_DOWN:
                    y_change=0
        y+=y_change
        gameDisplay.fill(white)
        ship(x,y)

        if y > display_height-ship_height or y<0:
            crash()
        pygame.display.update()
        #How fast are we going to target Frames per second
        clock.tick(60)
game_loop()
pygame.quit()
quit()