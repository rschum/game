from source.abstract.chemistry.rock import rock
from source.chemistry.chemicals import water
from source.chemistry.composition.composition import Composition


class Ice(rock.Rock):

    def __init__(self):
        rock.Rock.__init__(self)
        self.name = "Ice"
        self.composition = Composition([(1, water.Water())])
        pass
