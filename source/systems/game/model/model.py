from source.abstract.app.model import model

from source.systems.entity_factory import entity_factory

from source.systems.location.planet import planet

class Model(model.Model):
    entity_factory = None

    def __init__(self, parent = None):
        model.Model.__init__(self)
        self.entity_factory = entity_factory.EntityFactory(self)
        #self.universe = planet.Planet(self)
        pass

    def get_app(self):
        return self
