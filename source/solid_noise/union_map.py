import numpy
from matplotlib import pyplot
from opensimplex import OpenSimplex
import math
import base_map
import noise_map

class UnionMap(base_map.BaseMap):
    complexity = 1
    octaves = []
    def __init__(self, parent = None, seed = 0):
        base_map.BaseMap.__init__(self, parent, seed)

    def refresh(self):
        base_map.BaseMap.refresh(self)

        for i in range(self.complexity):
            octave = noise_map.NoiseMap(self)
            octave.seed         = self.seed + i+1
            octave.frequency    = self.frequency * 2 * i+1
            octave.amplitude    = 1
            octave.refresh()
            self.octaves.append(octave)
        pass

    def populate_noise_map(self, ix, iy, nx, ny):
        self.noise_map[iy][ix] = self.get_noise(nx, ny)
        pass

    def get_noise(self, nx, ny):
        z = []
        for octave in self.octaves:
            z.append(octave.get_noise(nx, ny))
        s = sum(z)
        return s

    def get_z(self, nx, ny):
        value = self.get_noise(nx, ny)
        amplified = 1 #math.pow(value, self.amplitude)
        difference = (self.max_value + abs(self.min_value))
        normal = difference * amplified - abs(self.min_value)
        return normal #return value between self.max_value and self.min_value
