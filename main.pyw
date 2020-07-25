from pygame import *
import math

default_x = 276
default_y = 8

my_height = 24
my_width = 84

# center_x = 300
# center_y = 300

radius = 254


class Round:
    def __init__(self, height, width):
        global default_x, default_y, radius

        self.position = 0
        self.x = default_x
        self.y = default_y

        self.height = height
        self.width = width

        self.sprite = image.load("sprite/player.png").subsurface(0, 0, width, height)
        self.rect = Rect(self.x, self.y, width, height)

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def move(self, path, screen):
        self.sprite = transform.rotate(image.load("sprite/player.png").subsurface(0, 0, self.width, self.height),
                                       self.position)
        self.position = (self.position + 360 + path) % 360

        print(self.position)

        if 90 <= self.position < 180:
            angle_sin = -math.sin(math.radians(self.position - 90))
            angle_cos = math.cos(math.radians(self.position - 90))
        elif self.position >= 270:
            angle_sin = -math.sin(math.radians(self.position - 90))
            angle_cos = math.cos(math.radians(self.position - 90))
        else:
            angle_sin = math.sin(math.radians(self.position))
            angle_cos = math.cos(math.radians(self.position))

        if self.position < 90:
            start_x, start_y = 254, 8
            center_x = center_y = 300
        elif self.position < 180:
            start_x, start_y = 8, 254
            center_x, center_y = 300, 300
        elif self.position < 270:
            start_x, start_y = 346, 24
            center_x = center_y = 300
        else:
            start_x, start_y = 24, 346
            center_x = center_y = 300

        self.x = center_x + int((start_x - center_x) * angle_cos + (start_y - center_y) * angle_sin)
        self.y = center_y + int((start_x - center_x) * angle_sin + (start_y - center_y) * angle_cos)

        self.rect = Rect(self.x, self.y, self.width, self.height)
        screen.blit(self.sprite, (self.x, self.y))


class Tile:
    pass


class Game:
    def __init__(self):
        global my_height, my_width
        self.clock = time.Clock()
        init()
        display.set_caption("RoundBall Z")
        self.screen = display.set_mode((600, 600))
        self.tiles = []
        self.round = Round(my_height, my_width)
        self.speed = 0

    def draw(self):
        self.screen.fill([0, 0, 0])
        self.round.draw(self.screen)
        draw.circle(self.screen, (255, 255, 255), (300, 300), 300, 8)
        draw.circle(self.screen, (255, 0, 0), (300, 300), 260, 8)
        display.flip()

    def start(self):
        finished = False
        while not finished:
            self.clock.tick(80)
            for ev in event.get():
                if ev.type == QUIT:
                    finished = True
                elif ev.type == KEYDOWN:
                    if ev.key == K_RIGHT:
                        self.speed = -1
                    elif ev.key == K_LEFT:
                        self.speed = 1
                elif ev.type == KEYUP:
                    self.speed = 0
            self.round.move(self.speed, self.screen)
            self.draw()


game = Game()
game.start()
