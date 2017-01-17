from source.abstract.entities.inanimate.model import model

from pygame import math

class Model(model.Model):
    name    = "Tile"
    mined   = False

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.dimensions = math.Vector3(100, 100, 100)
        self.radius = self.dimensions.x / 2
        self.mass = 100
        pass

    def mine_ore(self):
        if self.mined == False:
            from source.concrete.entities.inanimate.rock import rock
            from source.library.science.geology.rocks import bauxite
            ore = self.entity_manager.spawn(rock.Rock, None)
            ore.mass = 100
            ore.set_material(bauxite.Bauxite())
            self.mined = True
            return ore
        else:
            return None
        return None

    def north(self):
        pass

    def east(self):
        pass

    def south(self):
        pass

    def west(self):
        pass

    def get_tile(self, position = None):
        return self
