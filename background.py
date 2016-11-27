import pygame, random, globalvars

class BackgroundManager(pygame.sprite.Sprite):
    stars = []
    last_stars = []

    def __init__(self):
        self.star_color = globalvars.star_color
        for x in range(globalvars.init_stars):
            self.add_star()

    def update(self):
        for counter, star in enumerate(self.stars):
            if star.top > globalvars.WIN_RESY:
                del self.stars[counter]
                del self.last_stars[counter]
                self.add_star()
            else:
                self.last_stars[counter].top = star.top
                star.top += star.speed
                # print "%s %s"%(star,self.last_stars[counter])

    def draw(self):
        for star in self.stars:
            globalvars.surface.fill(self.star_color, star)
        return self.stars

    def clear(self):
        for star in self.last_stars:
            globalvars.surface.fill(globalvars.bgcolor, star)
        return self.last_stars

    def add_star(self):
        size = random.randint(3, 6)
        x = random.randint(0, globalvars.WIN_RESX)
        rect = star(x, 0, size, size)
        rect.set_speed(random.randint(2, globalvars.BG_Speed))
        self.stars.append(rect)
        self.last_stars.append(pygame.Rect(rect))


class star(pygame.Rect):
    def set_speed(self, tspeed):
        self.speed = tspeed

    def get_speed(self):
        return self.speed

