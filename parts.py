class Part(object):
    def __init__(self):
        self.active = False
        self.cubes = []

    def update(self):
        self.active = self.input_active()
        for cube in self.cubes:
            if cube.function == "WIRE":
                cube.active = self.active
            cube.update()

    def input_active(self):
        for cube in self.cubes:
            if cube.function == "INPUT":
                return cube.active
        return False

    def add(self, cube):
        self.cubes.append(cube)

    def add_multiple(self, cubes):
        for cube in cubes:
            self.add(cube)

    def delete(self, coords):
        cube = self.find_at(coords)
        self.cubes.pop(cube)

    def find_at(self, coords):
        for cube in self.cubes:
            if cube.coords == coords:
                return self.cubes.index(cube)
        return None

    def find_cube(self, cube_to_find):
        for cube in self.cubes:
            if cube is cube_to_find:
                return self.cubes.index(cube)
        return None

    def draw(self):
        for cube in self.cubes:
            cube.draw()
            print(cube.active)