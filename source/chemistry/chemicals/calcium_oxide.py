from source.chemistry.element import elements
from source.chemistry.chemical import chemical


class Calcium_oxide(chemical.Chemical):

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.name = "Calcium_oxide"
        self.mass = 56.08
        self.density = 3.34
        self.elements = [
            elements.Calcium(),
            elements.Oxygen(),
        ]
        self.formula = "CaO"
        pass
