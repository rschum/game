from source.abstract.location.model import model
from source.systems.location.solar_system import solar_system

class Model(model.Model):
    solar_system    = None

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.solar_system = solar_system.SolarSystem(self)
        pass
