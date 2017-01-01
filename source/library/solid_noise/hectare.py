import solid_noise

class HectareMap(solid_noise.NoiseMap):
    #seed = 2

    #min_value = -100.0
    #max_value =  100.0

    def __init__(self, parent = None, x_axis = 0, y_axis = 0):
        solid_noise.NoiseMap.__init__(self, parent, x_axis, y_axis)
        pass
