import pygame
from pygame.math import Vector2
import cube
import cubes

def run():
    #settings
    window_width, window_height = 1600, 900
    window = pygame.display.set_mode((window_width, window_height))
    rows, columns = int(window_width / cube.width), int(window_height / cube.width)

    clock = pygame.time.Clock()

    #mouse
    mouse_clicked = False

    #cubes
    cube.window = window
    selected_cube = "WIRE"

    def create_cube():
        mouse_pos = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        coords = cube.check_pos(mouse_pos)
        if selected_cube == "INPUT":
            new_cube = cube.Cube_input(coords)
        elif selected_cube == "VAR":
            new_cube = cube.Cube_var(coords)
        elif selected_cube == "WIRE":
            new_cube = cube.Cube_wire(coords)
        cubes.add(new_cube)

    while True:
        clock.tick(20)

        if mouse_clicked:
            create_cube()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_clicked = True
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_clicked = False

        cubes.update()

        cubes.draw()

        pygame.display.update()