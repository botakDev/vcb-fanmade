import pygame
from pygame.math import Vector2

#settings
window = pygame.surface.Surface((1, 1))

width = 30
height = 30

#colors
GRAY = pygame.color.Color(41, 41, 41)
RED = pygame.color.Color(161, 31, 41)
RED_INACTIVE = pygame.color.Color(54, 18, 21)
GREEN = pygame.color.Color(93, 168, 89)
GREEN_INACTIVE = pygame.color.Color(87, 112, 85)
YELLOW = pygame.color.Color(222, 222, 146)
YELLOW_INACTIVE = pygame.color.Color(71, 71, 48)

def check_pos(pos):
    return Vector2(round(pos.x / width - 1, 0), round(pos.y / height - 1, 0))

def calc_pos(coords):
    pos = Vector2(coords.x * width + width / 2, coords.y * height + height / 2)
    return pos

class Cube_wire(object):
    def __init__(self, coords):
        self.active = True
        self.color = YELLOW
        self.pos = calc_pos(coords)

        self.image = pygame.surface.Surface((width, height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        if self.active:
            self.color = YELLOW
        else:
            self.color = YELLOW_INACTIVE

        self.image.fill(self.color)

    def draw(self):
        window.blit(self.image, self.pos)
        pygame.draw.rect(window, self.color, self.rect)

class Cube_input(object):
    def __init__(self, coords):
        self.active = True
        self.color = RED
        self.pos = calc_pos(coords)

        self.image = pygame.surface.Surface((width, height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        if self.active:
            self.color = RED
        else:
            self.color = RED_INACTIVE

        self.image.fill(self.color)

    def draw(self):
        window.blit(self.image, self.pos)
        pygame.draw.rect(window, self.color, self.rect)

class Cube_var(object):
    def __init__(self, coords):
        self.active = True
        self.color = GREEN
        self.pos = calc_pos(coords)

        self.image = pygame.surface.Surface((width, height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        if self.active:
            self.color = GREEN
        else:
            self.color = GREEN

        self.image.fill(self.color)

    def draw(self):
        window.blit(self.image, self.pos)
        pygame.draw.rect(window, self.color, self.rect)
