class Part(object):
    def __init__(self, function):
        self.function = function
        self.active = False
        self.cubes = []

    def update(self):
        for cube in self.cubes:
            cube_id = self.cubes.index(cube)
            if self.function != "VAR":
                self.cubes[cube_id].active = self.active
            self.cubes[cube_id].update()

    def add(self, cube):
        self.cubes.append(cube)
        if cube.function == "VAR":
            self.active = True

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