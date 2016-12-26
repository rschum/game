from source.chemistry.element import elements
from source.chemistry.chemical import chemical


class Hematite(chemical.Chemical):

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.name = "Hematite"
        self.mass = 159.70
        self.density = 5.26
        self.elements = [
            elements.Iron(),
            elements.Iron(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen()
        ]
        self.formula = "Fe(III)2O3"
        pass
