import pygame
from pygame.math import Vector2
import cube
import cubes
import colors

# settings
window_width, window_height = 1600, 900
window = pygame.display.set_mode((window_width, window_height))
rows, columns = int(window_width / cube.width), int(window_height / cube.width)

clock = pygame.time.Clock()

# game
game_run = True

# input
input_update = True

# cubes
cube.window = window
selected_cube = "WIRE"
delete_on = False


def create_cube():
    mouse_pos = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    coords = cube.calc_coords(mouse_pos)
    if selected_cube == "INPUT":
        new_cube = cube.Cube_input(coords)
    elif selected_cube == "VAR":
        new_cube = cube.Cube_var(coords)
    elif selected_cube == "WIRE":
        new_cube = cube.Cube_wire(coords)
    elif selected_cube == "NOT":
        new_cube = cube.Cube_not(coords)
    if cubes.find_at(coords) is None:
        cubes.add(new_cube)


def delete_cube():
    mouse_pos = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    coords = cube.calc_coords(mouse_pos)
    if cubes.find_at(coords) is not None:
        cubes.delete(coords)


class Button(object):
    def __init__(self, pos, function, type, color, size, surface_pos):
        self.pos = pos
        self.function = function
        self.type = type
        self.color = color

        self.image = pygame.surface.Surface(size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos + surface_pos

    def update_color(self, color):
        self.color = color
        self.image.fill(self.color)

    def on_click(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def draw(self, surface):
        pygame.draw.rect(surface, "BLACK", self.rect)
        surface.blit(self.image, self.pos)


class Panel(object):
    def __init__(self, pos, width, height):
        self.panel_surface = pygame.surface.Surface((width, height))
        self.pos = pos
        self.buttons = []

    def add_btn(self, btn):
        self.buttons.append(btn)

    def clicked(self):
        for i in range(len(self.buttons)):
            if self.buttons[i].on_click():
                return self.buttons[i]
        return False

    def change_btn_color(self, function, type, color):
        for i in range(len(self.buttons)):
            if self.buttons[i].function == function and self.buttons[i].type == type:
                self.buttons[i].color = color
                self.buttons[i].update_color(color)
                break

    def draw(self):
        for i in range(len(self.buttons)):
            self.buttons[i].draw(self.panel_surface)
        window.blit(self.panel_surface, self.pos)


# panel
bottom_panel = Panel(Vector2(0, 800), 1600, 100)
input_btn = Button(Vector2(25, 25), "INPUT", "CUBE_TYPE", colors.RED, (50, 50), bottom_panel.pos)
bottom_panel.add_btn(input_btn)
var_btn = Button(Vector2(75, 25), "VAR", "CUBE_TYPE", colors.GREEN, (50, 50), bottom_panel.pos)
bottom_panel.add_btn(var_btn)
wire_btn = Button(Vector2(125, 25), "WIRE", "CUBE_TYPE", colors.YELLOW, (50, 50), bottom_panel.pos)
bottom_panel.add_btn(wire_btn)
not_btn = Button(Vector2(175, 25), "NOT", "CUBE_TYPE", colors.BLUE, (50, 50), bottom_panel.pos)
bottom_panel.add_btn(not_btn)
delete_btn = Button(Vector2(225, 25), "DEL", "FUNCTION", colors.WHITE, (50, 50), bottom_panel.pos)
bottom_panel.add_btn(delete_btn)
run_btn = Button(Vector2(325, 25), "RUN", "FUNCTION", colors.GREEN_LIGHT, (50, 50), bottom_panel.pos)
bottom_panel.add_btn(run_btn)

# mouse
mouse_clicked = False

while True:
    clock.tick(60)
    events = pygame.event.get()

    if game_run:
        cubes.update()
    if mouse_clicked:
        if pygame.mouse.get_pos()[1] < 790:
            if delete_on:
                delete_cube()
            else:
                create_cube()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_clicked = False
            if bottom_panel.clicked() != False:
                if bottom_panel.clicked().type == "CUBE_TYPE":
                    selected_cube = bottom_panel.clicked().function
                    delete_on = False
                elif bottom_panel.clicked().type == "FUNCTION":
                    if bottom_panel.clicked().function == "DEL":
                        delete_on = True
                    elif bottom_panel.clicked().function == "RUN":
                        game_run = not game_run
                        if game_run:
                            cubes.reset_cubes()
                            bottom_panel.change_btn_color("RUN", "FUNCTION", colors.RED_DARK)
                        else:
                            bottom_panel.change_btn_color("RUN", "FUNCTION", colors.GREEN_LIGHT)

    window.fill(colors.BLACK)

    bottom_panel.draw()
    cubes.draw()

    pygame.display.update()
