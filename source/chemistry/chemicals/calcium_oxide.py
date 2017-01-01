from source.chemistry.element import elements
from source.abstract.chemistry.chemical import chemical


class Calcium_oxide(chemical.Chemical):
    name = "Calcium_oxide"
    molar_mass = 56.08
    density = 3.34
    formula = "CaO"

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            elements.Calcium(),
            elements.Oxygen(),
        ]
        pass
