from source.chemistry.element import elements
from source.chemistry.chemical import chemical


# FeO
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
