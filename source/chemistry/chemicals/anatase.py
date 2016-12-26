from source.chemistry.element import elements
from source.chemistry.chemical import chemical


class Anatase(chemical.Chemical):

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.name = "Anatase"
        self.mass = 79.88
        self.density = 3.9
        self.elements = [
            elements.Titanium(),
            elements.Oxygen(),
            elements.Oxygen(),
        ]
        self.formula = "TiO2"
        pass
