from source.chemistry.element import elements
from source.abstract.chemistry.chemical import chemical


class Anatase(chemical.Chemical):
    name = "Anatase"
    molar_mass = 79.88
    density = 3.9
    formula = "TiO2"

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            elements.Titanium(),
            elements.Oxygen(),
            elements.Oxygen(),
        ]
        pass
