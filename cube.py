import pygame
from pygame.math import Vector2
import colors
import cubes

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
        self.function = "WIRE"

        self.image = pygame.surface.Surface((width, height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

        self.part_id = None

    def update_color(self):
        if self.active:
            self.color = colors.YELLOW
        else:
            self.color = colors.YELLOW_INACTIVE

        self.image.fill(self.color)

    def update(self):
        self.update_color()

        top = cubes.get_top(self.coords)
        bottom = cubes.get_bottom(self.coords)
        left = cubes.get_left(self.coords)
        right = cubes.get_right(self.coords)

        if cubes.find_at(top) is not None:
            if cubes.get_part(top).function == "INPUT":
                cubes.set_active(self.coords, cubes.get_part(top).active)
                return
        if cubes.find_at(bottom) is not None:
            if cubes.get_part(bottom).function == "INPUT":
                cubes.set_active(self.coords, cubes.get_part(bottom).active)
                return
        if cubes.find_at(left) is not None:
            if cubes.get_part(left).function == "INPUT":
                cubes.set_active(self.coords, cubes.get_part(left).active)
                return
        if cubes.find_at(right) is not None:
            if cubes.get_part(right).function == "INPUT":
                cubes.set_active(self.coords, cubes.get_part(right).active)
                return

    def draw(self):
        window.blit(self.image, self.pos)
        pygame.draw.rect(window, self.color, self.rect)

class Cube_input(object):
    def __init__(self, coords):
        self.active = True
        self.color = colors.RED
        self.pos = calc_pos(coords)
        self.coords = coords
        self.function = "INPUT"

        self.image = pygame.surface.Surface((width, height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update_color(self):
        if self.active:
            self.color = colors.RED
        else:
            self.color = colors.RED_INACTIVE

        self.image.fill(self.color)

    def update(self):
        self.update_color()

        top = cubes.get_top(self.coords)
        bottom = cubes.get_bottom(self.coords)
        left = cubes.get_left(self.coords)
        right = cubes.get_right(self.coords)

        if cubes.find_at(top) is not None:
            if cubes.get_part(top).function == "VAR":
                cubes.set_active(self.coords, cubes.get_part(top).active)
                return
        if cubes.find_at(bottom) is not None:
            if cubes.get_part(bottom).function == "VAR":
                cubes.set_active(self.coords, cubes.get_part(bottom).active)
                return
        if cubes.find_at(left) is not None:
            if cubes.get_part(left).function == "VAR":
                cubes.set_active(self.coords, cubes.get_part(left).active)
                return
        if cubes.find_at(right) is not None:
            if cubes.get_part(right).function == "VAR":
                cubes.set_active(self.coords, cubes.get_part(right).active)
                return
        if cubes.get_part(self.coords).active == False:
            cubes.set_active(self.coords, False)

    def draw(self):
        window.blit(self.image, self.pos)
        pygame.draw.rect(window, self.color, self.rect)

class Cube_var(object):
    def __init__(self, coords):
        self.active = True
        self.color = colors.GREEN
        self.pos = calc_pos(coords)
        self.coords = coords
        self.function = "VAR"

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

class Cube_not(object):
    def __init__(self, coords):
        self.active = False
        self.color = colors.BLUE
        self.pos = calc_pos(coords)
        self.coords = coords
        self.function = "NOT"

        self.image = pygame.surface.Surface((width, height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        if self.active:
            self.color = colors.BLUE

        self.image.fill(self.color)

    def draw(self):
        window.blit(self.image, self.pos)
        pygame.draw.rect(window, self.color, self.rect)