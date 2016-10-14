import pygame
#Lets Set up our window
pygame.init()
display_width=800
display_height=600
#RGB colors
black=(0,0,0)
white=(255,255,255)
gameDisplay =pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Shooter Dude") #Changes the title of the window
clock=pygame.time.Clock()

shipIMG= pygame.image.load('ship')
def ship(x,y):
    gameDisplay.blit(shipIMG,(x,y))
x=0
y=(display_height*0.5)
y_change=0
#So the user has to X out in order to exit the window
crashed=False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed =True
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
    pygame.display.update()
    #How fast are we going to target Frames per second
    clock.tick(60)

pygame.quit()
quit()