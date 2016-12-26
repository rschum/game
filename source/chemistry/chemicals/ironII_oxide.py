from source.chemistry.element import elements
from source.chemistry.chemical import chemical


# FeO
class IronIIOxide(chemical.Chemical):

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.name = "IronII Oxide"
        self.mass = 71.85
        self.density = 5.75
        self.elements = [
            elements.Iron(),
            elements.Oxygen(),
        ]
        self.formula = "FeO"
        pass
