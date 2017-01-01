import solid_noise, kilometer

class PlanetMap(solid_noise.NoiseMap):
    radius = 50

    min_value = -10911.00
    max_value =  8848.00

    #octaves = 2

    #frequency = 1

    def __init__(self, parent = None, x_axis = 0, y_axis = 0):
        solid_noise.NoiseMap.__init__(self, parent, x_axis, y_axis)
        #self.octave = kilometer.KilometerMap(self)
        self.octaves = [
            solid_noise.NoiseMap(self),
            solid_noise.NoiseMap(self)
        ]
        pass
