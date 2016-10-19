import pygame
import time
import random


pygame.init()
display_width=1000
display_height=600
#RGB colors
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

ship_height= 72
ship_width=94
gameDisplay =pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Planet Parenthood") #Changes the title of the window
clock=pygame.time.Clock()
shipIMG= pygame.image.load('ship')
enemyIMG=pygame.image.load('enemies')
gameIcon = pygame.image.load('logo.jpg')

def things(thingx,thingy, thingw,thingh,color,enemyIMG):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    gameDisplay.blit(enemyIMG, (thingx, thingy))

def ship(x,y):
    gameDisplay.blit(shipIMG,(x,y))
def text_objects(text, font):
    textSurface=font.render(text, True,black)
    return textSurface, textSurface.get_rect()
def crash():
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()


def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def paused():
    ############
    pygame.mixer.music.pause()
    #############
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue", 150, 450, 100, 50, green, bright_green, unpause)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("Planet Parenthood", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    x=0
    y=(display_height*0.5)
    y_change=0
    thing_startx= 999
    thing_starty= random.randrange(0,display_height)
    thing_speed=-8
    thing_height = 94
    thing_width = 90
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

        things(thing_startx, thing_starty, thing_width, thing_height, black, enemyIMG)
        thing_startx+=thing_speed

        ship(x,y)
        if y > display_height-ship_height or y<0:
            crash()
        if thing_startx < 0:
            thing_startx=display_width
            thing_starty=random.randrange(0,display_height)
        if x <thing_startx+thing_width:
            print('x crossover')
            #if y>thing_starty and y< thing_starty + thing_height or y+ship_height> thing_starty and x+ship_width<thing_startx+thing_width:
                #crash()
        pygame.display.update()
        #How fast are we going to target Frames per second
        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()