from source.abstract.location.model import model
from source.concrete.entities.inanimate.tile import tile

from pygame import math

class Model(model.Model):
    size  = 10
    tiles = None

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        tiles = [[]]
        self.name = "Hectare"
        self.dimensions = math.Vector3(10000, 10000, 10000)
        self.radius = self.dimensions.x / 2
        self.populate_tiles()
        pass

    def north(self):
        pass

    def east(self):
        pass

    def south(self):
        pass

    def west(self):
        pass

    def get_hectare(self):
        return self

    def get_kilometer(self):
        return self.parent.get_kilometer()

    def get_planet(self):
        return self.parent.get_planet()

    def get_tile(self, x, y):
        if x < self.size and y < self.size:
            if self.tiles[x][y] == None:
                self.tiles[x][y] = self.entity_manager.spawn(tile.Tile, self)
                self.tiles[x][y].position.x = (x * self.tiles[x][y].dimensions.x)
                self.tiles[x][y].position.y = (y * self.tiles[x][y].dimensions.y)
            return self.tiles[x][y].get_tile()
        return None
    
    def populate_tiles(self):
        self.tiles = [
            [
                None for x in range(self.size)
            ] for y in range(self.size)
        ]
        pass
    
    def get_tiles(self, a):
        x = a[0]
        y = a[1]
        w = a[2]
        h = a[3]

        if x <= 0:
            x = 0
        if y <= 0:
            y = 0

        tmp_tiles = [[self.get_tile(k, l) for k in range(x, x+w)] for l in range(y, y+h)]
        return tmp_tiles

    def convert_pixel_dimensions_to_tile_dimensions(self, a, b, c, d):
        tile = self.get_tile(0, 0).dimensions
        x = int((a - (c / 2)) / tile.x)
        y = int((b - (d / 2)) / tile.y)
        w = int((c + (c)) / tile.x) + 1
        h = int((d + (d)) / tile.y) + 1
        return (x, y, w, h)
    
    def get_near_tiles(self, object):
        return self.get_tiles(
            self.convert_pixel_dimensions_to_tile_dimensions(
                object.position.x,
                object.position.y,
                object.dimensions.x,
                object.dimensions.y
            )
        )
        pass
