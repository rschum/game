from source.chemistry.element import elements
from source.chemistry.chemical import chemical


class Silica(chemical.Chemical):

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.name = "Silica"
        self.mass = 60.09
        self.density = 2.65
        self.elements = [
            elements.Silicon(),
            elements.Oxygen(),
            elements.Oxygen(),
        ]
        self.formula = "SiO2"
        pass
