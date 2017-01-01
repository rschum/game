from source.chemistry.element import elements
from source.abstract.chemistry.chemical import chemical


class Hematite(chemical.Chemical):
    name = "Hematite"
    molar_mass = 159.70
    density = 5.26
    formula = "Fe(III)2O3"

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            elements.Iron(),
            elements.Iron(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen()
        ]
        pass
