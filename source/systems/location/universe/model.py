from source.abstract.location.model import model
from source.systems.location.galaxy import galaxy

class Model(model.Model):
    galaxy  = None

    def __init__(self, parent = None):
        model.Model.__init__(self)
        self.galaxy = galaxy.Galaxy(self)
        pass
