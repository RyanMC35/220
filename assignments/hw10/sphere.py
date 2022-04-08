from math import pi


class Sphere:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        surfacearea = 4 * pi * (self.radius ** 2)
        return surfacearea

    def volume(self):
        volume_ = (4/3) * pi * (self.radius ** 3)
        return volume_
