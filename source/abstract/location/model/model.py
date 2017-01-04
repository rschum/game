class Model:
    parent      = None
    entities    = []

    def __init__(self, parent = None):
        self.parent = parent
        pass

    def add_entity(self, object):
        self.entities.append(object)

    def remove_entity(self, object):
        self.entities.remove(object)
