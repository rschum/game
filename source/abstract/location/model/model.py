from pygame import math
from source.abstract.base_object.model import model

class Model(model.Model):
    postition   = None
    dimensions  = None
    index       = (0, 0)

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.position = math.Vector3(0, 0, 0)
        self.dimensions = math.Vector3(0, 0, 0)
        pass

    def get_position(self):
        self.position = math.Vector3(
            self.index[0] * self.dimensions.x,
            self.index[1] * self.dimensions.y,
            0
        )
        return self.position
