import pygame
from pygame.math import Vector2
import colors

#settings
window = pygame.surface.Surface((1, 1))

width = 30
height = 30

def calc_coords(pos):
    return Vector2(round(pos.x / width - 1, 0), round(pos.y / height - 1, 0))

def calc_pos(coords):
    return Vector2(coords.x * width + width / 2, coords.y * height + height / 2)

class Cube_wire(object):
    def __init__(self, coords):
        self.active = False
        self.color = colors.YELLOW
        self.pos = calc_pos(coords)
        self.coords = coords

        self.image = pygame.surface.Surface((width, height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        if self.active:
            self.color = colors.YELLOW
        else:
            self.color = colors.YELLOW_INACTIVE

        self.image.fill(self.color)

    def draw(self):
        window.blit(self.image, self.pos)
        pygame.draw.rect(window, self.color, self.rect)

class Cube_input(object):
    def __init__(self, coords):
        self.active = True
        self.color = colors.RED
        self.pos = calc_pos(coords)
        self.coords = coords

        self.image = pygame.surface.Surface((width, height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        if self.active:
            self.color = colors.RED
        else:
            self.color = colors.RED_INACTIVE

        self.image.fill(self.color)

    def draw(self):
        window.blit(self.image, self.pos)
        pygame.draw.rect(window, self.color, self.rect)

class Cube_var(object):
    def __init__(self, coords):
        self.active = False
        self.color = colors.GREEN
        self.pos = calc_pos(coords)
        self.coords = coords

        self.image = pygame.surface.Surface((width, height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        if self.active:
            self.color = colors.GREEN
        else:
            self.color = colors.GREEN_INACTIVE

        self.image.fill(self.color)

    def draw(self):
        window.blit(self.image, self.pos)
        pygame.draw.rect(window, self.color, self.rect)
