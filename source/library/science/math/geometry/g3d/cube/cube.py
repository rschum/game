from ..primitive_3d import primitive_3d

class Cube(primitive_3d.Primitive3D):
    width       = 1
    length      = 1
    height      = 1

    def __init__(self):
        primitive_3d.Primitive3D.__init__(self)
        pass

    def get_nodes(self):
        cube_nodes = [
            (x,y,z) for x in (
                0 + self.position.x,
                self.width + self.position.x
            ) for y in (
                0  + self.position.y,
                self.length + self.position.y
            ) for z in (
                0  + self.position.z,
                self.height + self.position.z
            )
        ]
        return cube_nodes
