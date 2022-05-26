from pygame.math import Vector2

cubes = []

def add(new_cube):
    coords = new_cube.coords
    cubes.append(new_cube)


    update_env(coords + Vector2(0, -1))
    update_env(coords + Vector2(0, 1))
    update_env(coords + Vector2(-1, 0))
    update_env(coords + Vector2(1, 0))
    update_env(coords)

def remove_at(coords):
    for i in range(len(cubes)):
        if cubes[i].coords == coords:
            cubes.pop(i)
            break

    for i in range(len(cubes)):
        cube_coords = cubes[i].coords
        update_env(cube_coords + Vector2(0, -1))
        update_env(cube_coords + Vector2(0, 1))
        update_env(cube_coords + Vector2(-1, 0))
        update_env(cube_coords + Vector2(1, 0))
        update_env(cube_coords)

def find_at(coords):
    for i in range(len(cubes)):
        if cubes[i].coords == coords:
            return i
    return False

def reset_cubes():
    for i in range(len(cubes)):
        if cubes[i].function == "WIRE":
            cubes[i].active = False

def turn_on_cubes():
    for i in range(len(cubes)):
        cubes[i].active = True

def update_env(coords):
    cube_id = find_at(coords)
    if cube_id is not False:
        cubes[cube_id].top_cube = find_at(coords + Vector2(0, -1))
        cubes[cube_id].bottom_cube = find_at(coords + Vector2(0, 1))
        cubes[cube_id].left_cube = find_at(coords + Vector2(-1, 0))
        cubes[cube_id].right_cube = find_at(coords + Vector2(1, 0))


def update():
    for cube in cubes:
        cube.update()

    for j in range(len(cubes)):
        for i in range(len(cubes)):
            cube = cubes[i]

            if cube.active:
                if cube.top_cube is not False:
                    cubes[cube.top_cube].active = True
                if cube.bottom_cube is not False:
                    cubes[cube.bottom_cube].active = True
                if cube.left_cube is not False:
                    cubes[cube.left_cube].active = True
                if cube.right_cube is not False:
                    cubes[cube.right_cube].active = True


def draw():
    for cube in cubes:
        cube.draw()
