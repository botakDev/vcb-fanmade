from pygame.math import Vector2
import parts

part_list = []

def get_top(coords):
    return coords + Vector2(0, -1)


def get_bottom(coords):
    return coords + Vector2(0, 1)


def get_left(coords):
    return coords + Vector2(-1, 0)


def get_right(coords):
    return coords + Vector2(1, 0)

def add(new_cube):
    coords = new_cube.coords
    new_part(new_cube)

    for _ in range(4):
        check_touching_parts(coords)
    print(part_list)


def new_part(cube):
    new_part = parts.Part(cube.function)
    new_part.add(cube)
    part_list.append(new_part)


def delete(coords):
    part_id = find_part(coords)
    part_list[part_id].delete(coords)
    try_split_part(part_id)


def find_at(coords):
    for part in part_list:
        if part.find_at(coords) is not None:
            return part.find_at(coords)
    return None


def find_part(coords):
    for part in part_list:
        if part.find_at(coords) is not None:
            return part_list.index(part)
    return None


def find_cube(cube_to_find):
    for part in part_list:
        if part.find_cube(cube_to_find) is not None:
            return part.find_cube(cube_to_find)
    return None

def get_part(coords):
    for part in part_list:
        if part.find_at(coords) is not None:
            return part


def set_active(coords, active):
    part_list[find_part(coords)].active = active


def check_touching_parts(coords):
    top = get_top(coords)
    bottom = get_bottom(coords)
    left = get_left(coords)
    right = get_right(coords)

    if find_part(coords) is not find_part(top) \
            and find_part(top) is not None:
        if part_list[find_part(top)].function == part_list[find_part(coords)].function:
            connect_parts(find_part(coords), find_part(top))

    if find_part(coords) is not find_part(bottom) \
            and find_part(bottom) is not None:
        if part_list[find_part(bottom)].function == part_list[find_part(coords)].function:
            connect_parts(find_part(coords), find_part(bottom))

    if find_part(coords) is not find_part(left) \
            and find_part(left) is not None:
        if part_list[find_part(left)].function == part_list[find_part(coords)].function:
            connect_parts(find_part(coords), find_part(left))

    if find_part(coords) is not find_part(right) \
            and find_part(right) is not None:
        if part_list[find_part(right)].function == part_list[find_part(coords)].function:
            connect_parts(find_part(coords), find_part(right))


def connect_parts(part_id, target_part_id):
    giver_id = target_part_id
    target_id = part_id
    part_list[target_id].add_multiple(part_list[giver_id].cubes)
    part_list.pop(giver_id)


def try_split_part(part_id):
    main_part_id = part_id
    for cube in part_list[main_part_id].cubes:
        new_part(cube)
    part_list.pop(main_part_id)

    for part in part_list:
        for cube in part.cubes:
            check_touching_parts(cube.coords)


def update():
    for part in part_list:
        part.update()


def reset_cubes():
    for part in part_list:
        part_list[part_list.index(part)].active = False


def draw():
    for part in part_list:
        part.draw()
