class Model:
    name        = "Location"
    parent      = None
    entities    = []

    def __init__(self, parent = None):
        self.parent = parent
        pass

    def add_entity(self, object):
        object.parent = self
        self.entities.append(object)

    def remove_entity(self, object):
        object.parent = None
        self.entities.remove(object)
