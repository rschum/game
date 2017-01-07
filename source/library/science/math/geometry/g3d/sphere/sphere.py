from ..primitive_3d import primitive_3d

class Sphere(primitive_3d.Primitive3D):
    radius      = 1

    def __init__(self):
        primitive_3d.Primitive3D.__init__(self)
        pass

    def collide(self, object):
        distance = self.position.distance_to(object.position)
        if distance < self.radius + object.radius:
            return True
        return False
