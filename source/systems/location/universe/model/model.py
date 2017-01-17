from source.abstract.location.model import model
from source.systems.location.galaxy import galaxy

class Model(model.Model):
    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        pass

    def spawn(self):
        model.Model.spawn(self)
        self.entity_manager.spawn(galaxy.Galaxy, self)
        pass

    def get_app(self):
        return self.entity_manager.get_app()
