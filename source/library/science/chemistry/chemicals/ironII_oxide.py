from source.library.science.chemistry.element import elements
from source.abstract.chemistry.chemical import chemical


class IronIIOxide(chemical.Chemical):
    name = "IronII Oxide"
    molar_mass = 71.85
    density = 5.75
    formula = "FeO"

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            elements.Iron(),
            elements.Oxygen(),
        ]
        pass
