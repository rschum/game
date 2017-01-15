from source.abstract.entities.inanimate.model import model

class Model(model.Model):
    name        = "Rock"
    mass        = 100
    material    = None

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.radius = 16
        pass
