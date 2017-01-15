from source.abstract.location.model import model

from source.systems.location.hectare import hectare

from pygame import math

class Model(model.Model):
    size        = 1
    hectares    = None

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        hectares = [[]]
        self.dimensions = math.Vector3(100000, 100000, 0)
        self.radius = self.dimensions.x / 2
        pass

    def spawn(self):
        model.Model.spawn(self)
        self.populate_hectares()
        pass

    def populate_hectares(self):
        self.hectares = [
            [
                self.entity_factory.spawn(hectare.Hectare, self) for x in range(self.size)
            ] for y in range(self.size)
        ]
        pass

    def north(self):
        pass

    def east(self):
        pass

    def south(self):
        pass

    def west(self):
        pass

    def get_hectare(self, position):
        pos = position / 10
        x = int(math.floor(pos.x))
        y = int(math.floor(pos.y))
        if self.hectares[x][y] == None:
            self.hectares[x][y] = self.entity_factory.spawn(hectare.Hectare, self)
        return self.hectares[x][y]

    def get_kilometer(self):
        return self

    def get_planet(self):
        return self.parent.get_planet()

    def get_tile(self, position):
        pos = position / 100
        tile = self.get_hectare().get_tile(
            int(math.floor(pos.x)),
            int(math.floor(pos.y))
        )
        return tile
