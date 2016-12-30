import numpy
from matplotlib import pyplot
from opensimplex import OpenSimplex
import math

class Map:
    parent      = None
    seed        = 0
    x_axis      = 0
    y_axis      = 0
    min_value   = -1.0
    max_value   =  1.0
    x_offset    = 0
    y_offset    = 0
    z_offest    = 0
    frequency   = 1
    amplitude   = 1.000
    noise_map   = None
    #color_map   = 'gray'
    #color_map   = 'gist_heat'
    color_map   = 'terrain'

    def __init__(self, parent = None, seed = 0):
        self.parent = parent
        self.seed = seed
        pass

    def generate_noise_map(self):
        self.noise_map = numpy.zeros((self.y_axis, self.x_axis), dtype=float)
        pass

    def refresh(self):
        self.x_axis     = self.x_axis       if self.parent == None else self.parent.x_axis
        self.y_axis     = self.y_axis       if self.parent == None else self.parent.y_axis
        self.max_value  = self.max_value    if self.parent == None else self.parent.max_value
        self.min_value  = self.min_value    if self.parent == None else self.parent.min_value
        pass

    def show(self):
        plot = pyplot.matshow(self.noise_map, cmap=self.color_map)
        #pyplot.clim(vmin = self.min_value, vmax = self.max_value)
        pyplot.clim(vmin = 0, vmax = 1)
        pyplot.show()

class UnionMap(Map):
    complexity = 1
    octaves = []
    def __init__(self, parent = None, seed = 0):
        Map.__init__(self, parent, seed)

    def refresh(self):
        Map.refresh(self)

        for i in range(self.complexity):
            octave = NoiseMap(self)
            octave.seed = self.seed + i+1
            octave.frequency = self.frequency * 2 * i+1
            octave.refresh()
            self.octaves.append(octave)

    def generate_noise_map(self):
        Map.generate_noise_map(self)
        for octave in self.octaves:
            octave.generate_noise_map()
        pass

    def show(self):
        for octave in self.octaves:
            octave.show()
        pass

class NoiseMap(Map):
    generator = None

    def __init__(self, parent = None, seed = 0):
        Map.__init__(self, parent, seed)
        pass

    def refresh(self):
        Map.refresh(self)
        self.generator  = OpenSimplex(self.seed)
        print("asdf")
        pass

    def get_noise(self, nx, ny):
        value = 1.0/float(self.frequency) * self.generator.noise2d(self.frequency * nx, self.frequency * ny) / 2 + 0.5
        return value #A value between 0.0 and 1.0

    def get_z(self, nx, ny):
        value = self.get_noise(nx, ny)
        difference = (self.max_value + abs(self.min_value))
        normal = difference * value - abs(self.min_value)
        return normal #return value between self.max_value and self.min_value
    
    def generate_noise_map(self):
        Map.generate_noise_map(self)
        
        for iy in range(self.y_axis):
            for ix in range(self.x_axis):
                nx = float(ix)/float(self.x_axis) + self.x_offset
                ny = float(iy)/float(self.y_axis) + self.y_offset
                z = self.get_noise(nx, ny)
                self.noise_map[iy][ix] = z
        pass
