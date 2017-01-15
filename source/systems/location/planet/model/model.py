from pygame import math
from source.abstract.location.model import model
from source.library.ui.camera import camera
from source.systems.location.kilometer import kilometer
from source.systems.location.homestead import homestead
from source.concrete.entities.human.avatar import avatar

class Model(model.Model):
    camera          = None

    size            = 1
    kilometers      = [[]]

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.position = math.Vector3(0,0,0)
        self.dimensions = math.Vector3(100000, 100000, 100000)
        self.radius = self.dimensions.x / 2
        pass

    def spawn(self):
        model.Model.spawn(self)
        self.populate_kilometers()

    def populate_kilometers(self):
        self.kilometers = [[None for x in range(self.size)] for y in range(self.size)]

        for y in range(self.size):
            for x in range(self.size):
                k = self.entity_factory.spawn(kilometer.Kilometer, self)
                k.index = (x, y)
                self.kilometers[x][y] = k

    def get_planet(self):
        return self

    def get_kilometer(self):
        pass

    def get_hectare(self):
        pass

    def get_tile(self):
        pass
