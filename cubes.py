from pygame.math import Vector2
import parts

part_list = []

def add(new_cube):
    coords = new_cube.coords

    top = coords + Vector2(0, -1)
    bottom = coords + Vector2(0, 1)
    left = coords + Vector2(-1, 0)
    right = coords + Vector2(1, 0)

    if find_at(top) is not None:
            part_list[find_part(top)].add(new_cube)
    elif find_at(bottom) is not None:
            part_list[find_part(bottom)].add(new_cube)
    elif find_at(left) is not None:
            part_list[find_part(left)].add(new_cube)
    elif find_at(right) is not None:
            part_list[find_part(right)].add(new_cube)
    else:
        new_part = parts.Part()
        new_part.add(new_cube)
        part_list.append(new_part)

    for i in range(4):
        check_touching_parts(coords)

    print(part_list)

def delete(coords):
    part_list[find_part(coords)].delete(coords)

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

def check_touching_parts(coords):
    top = coords + Vector2(0, -1)
    bottom = coords + Vector2(0, 1)
    left = coords + Vector2(-1, 0)
    right = coords + Vector2(1, 0)

    if find_part(coords) is not find_part(top) \
            and find_part(top) is not None:
        split_parts(find_part(coords), find_part(top))

    if find_part(coords) is not find_part(bottom) \
            and find_part(bottom) is not None:
        split_parts(find_part(coords), find_part(bottom))

    if find_part(coords) is not find_part(left) \
            and find_part(left) is not None:
        split_parts(find_part(coords), find_part(left))

    if find_part(coords) is not find_part(right) \
            and find_part(right) is not None:
        split_parts(find_part(coords), find_part(right))


def split_parts(part_id, target_part_id):
    giver_id = target_part_id
    target_id = part_id
    part_list[target_id].add_multiple(part_list[giver_id].cubes)
    part_list.pop(giver_id)

def update():
    for part in part_list:
        part.update()

def reset_cubes():
    for part in part_list:
        part_list[part_list.index(part)].active = False

def draw():
    for part in part_list:
        part.draw()
