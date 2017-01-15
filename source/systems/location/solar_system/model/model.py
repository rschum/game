from source.abstract.location.model import model
from source.systems.location.planet import planet

class Model(model.Model):
    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        pass

    def spawn(self):
        model.Model.spawn(self)
        self.entity_factory.spawn(planet.Planet, self)
        pass
