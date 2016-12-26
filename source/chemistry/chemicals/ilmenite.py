from source.chemistry.element import elements
from source.chemistry.chemical import chemical


class Ilmenite(chemical.Chemical):

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.name = "Ilmenite"
        self.mass = 151.73
        self.density = 4.79
        self.elements = [
            elements.Iron(),
            elements.Titanium(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen()
        ]
        self.formula = "FeTiO3"  # FeO.TiO2
        pass

