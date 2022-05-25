from pygame.math import Vector2

cubes = []

def add(new_cube):
    cubes.append(new_cube)

def remove(index):
    cubes.pop(index)

def draw():
    for cube in cubes:
        cube.draw()

def find_at(coords):
    for i in range(len(cubes)):
        if cubes[i].coords == coords:
            return cubes[i]
    return None

def remove_at(coords):
    for i in range(len(cubes)):
        if cubes[i].coords == coords:
            remove(i)
            break

def update():
    for cube in cubes:
        cube.update()

    for i in range(len(cubes)):
        coords = cubes[i].coords
        top_cube = find_at(coords + Vector2(0, -1))
        bottom_cube = find_at(coords + Vector2(0, 1))
        left_cube = find_at(coords + Vector2(-1, 0))
        right_cube = find_at(coords + Vector2(1, 0))

        if (top_cube != None and top_cube.active) or \
                (bottom_cube != None and bottom_cube.active) or \
                (left_cube != None and left_cube.active) or \
                (right_cube != None and right_cube.active):
            cubes[i].active = True
