import numpy
from matplotlib import pyplot
from opensimplex import OpenSimplex
import math
import base_map

class NoiseMap(base_map.BaseMap):
    generator = None

    def __init__(self, parent = None, seed = 0):
        base_map.BaseMap.__init__(self, parent, seed)
        pass

    def load(self):
        base_map.BaseMap.load(self)
        self.generator  = OpenSimplex(self.seed)
        pass

    def get_noise(self, nx, ny):
        f = 1.0/float(self.frequency) if self.frequency != 0 else 0
        value = f * self.generator.noise2d(self.frequency * nx, self.frequency * ny) / 2 + 0.5
        return value
    
    def populate_noise_map(self, ix, iy, nx, ny):
        self.noise_map[iy][ix] = self.get_noise(nx, ny)
        pass
