import solid_noise, hectare

class KilometerMap(solid_noise.NoiseMap):
    #seed = 1

    #min_value = -10911.00
    #max_value =  8848.00

    #min_value = -1000.0
    #max_value =  1000.0

    def __init__(self, parent = None, x_axis = 0, y_axis = 0):
        solid_noise.NoiseMap.__init__(self, parent, x_axis, y_axis)
        #self.octave = hectare.HectareMap(self)
        pass
