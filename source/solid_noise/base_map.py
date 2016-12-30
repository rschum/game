import numpy
from matplotlib import pyplot
from sklearn.preprocessing import normalize
from opensimplex import OpenSimplex
import math

class BaseMap:
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
    amplitude   = 0
    noise_map   = None
    color_map   = 'gray'
    #color_map   = 'gist_heat'
    #color_map   = 'terrain'

    def __init__(self, parent = None, seed = 0):
        self.parent = parent
        self.seed = seed
        pass

    def generate_noise_map(self):
        self.noise_map = numpy.zeros((self.y_axis, self.x_axis), dtype=float)
        for iy in range(self.y_axis):
            for ix in range(self.x_axis):
                nx = float(ix)/float(self.x_axis) + self.x_offset
                ny = float(iy)/float(self.y_axis) + self.y_offset
                self.populate_noise_map(ix, iy, nx, ny)
        pass

    def normalize(self):
        self.noise_map = (self.noise_map - self.noise_map.min())/(self.noise_map.max() - self.noise_map.min())
        pass

    def populate_noise_map(self, ix, iy, nx, ny):
        pass

    def refresh(self):
        self.x_axis     = self.x_axis       if self.parent == None else self.parent.x_axis
        self.y_axis     = self.y_axis       if self.parent == None else self.parent.y_axis
        self.max_value  = self.max_value    if self.parent == None else self.parent.max_value
        self.min_value  = self.min_value    if self.parent == None else self.parent.min_value
        pass

    def show(self):
        plot = pyplot.matshow(self.noise_map, cmap=self.color_map)
        pyplot.clim(vmin = self.noise_map.min(), vmax = self.noise_map.max())
        pyplot.show()
        pass
