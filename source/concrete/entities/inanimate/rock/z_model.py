from source.abstract.entities.inanimate.model import model

class Model(model.Model):
    def __init__(self, parent, volume = 1, composition = None):
        model.Model.__init__(self, parent)
        self.volume = volume
        self.composition = composition
        pass
