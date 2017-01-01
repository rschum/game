from source.chemistry.element import elements
from source.abstract.chemistry.chemical import chemical


class Silica(chemical.Chemical):
    name = "Silica"
    molar_mass = 60.09
    density = 2.65
    formula = "SiO2"

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            elements.Silicon(),
            elements.Oxygen(),
            elements.Oxygen(),
        ]
        pass
