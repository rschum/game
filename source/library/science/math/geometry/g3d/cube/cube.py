from ..primitive_3d import primitive_3d

from pygame import math

class Cube(primitive_3d.Primitive3D):
    dimensions = None

    def __init__(self):
        primitive_3d.Primitive3D.__init__(self)
        self.dimensions = math.Vector3(1, 1, 1)
        pass

    def get_nodes(self):
        cube_nodes = [
            (x,y,z) for x in (
                0 + self.position.x,
                self.dimensions.x + self.position.x
            ) for y in (
                0  + self.position.y,
                self.dimensions.y + self.position.y
            ) for z in (
                0  + self.position.z,
                self.dimensions.z + self.position.z
            )
        ]
        return cube_nodes
