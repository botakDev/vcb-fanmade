cubes = []

def add(new_cube):
    for i in range(len(cubes)):
        if cubes[i].pos == new_cube.pos:
            cubes.pop(i)
    cubes.append(new_cube)
    print(cubes)

def remove(index):
    cubes.remove(index)

def update():
    for cube in cubes:
        cube.update()

def draw():
    for cube in cubes:
        cube.draw()