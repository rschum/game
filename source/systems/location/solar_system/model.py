from source.abstract.location.model import model
from source.systems.location.planet import planet

class Model(model.Model):
    planet = None

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.planet = planet.Planet(self)
        pass
