from source.library.science.chemistry.composition.composition import Composition

class View:
    def __init__(self):
        pass

    def pretty_print(self, i=0):
        print(("\t"*i) + self.name)
        Composition.pretty_print(self.composition, i+1)
