from source.abstract.entities.inanimate.model import model

class Model(model.Model):
    name    = "Tile"

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        pass

    def north(self):
        pass

    def east(self):
        pass

    def south(self):
        pass

    def west(self):
        pass
