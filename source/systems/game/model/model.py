from source.abstract.app.model import model

from source.systems.entity_manager import entity_manager

from source.systems.location.planet import planet

class Model(model.Model):
    entity_manager = None

    def __init__(self, parent = None):
        model.Model.__init__(self)
        self.entity_manager = entity_manager.EntityManager(self)
        pass

    def get_app(self):
        return self
