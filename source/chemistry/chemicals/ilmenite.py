from source.chemistry.element import elements
from source.abstract.chemistry.chemical import chemical


class Ilmenite(chemical.Chemical):
    name = "Ilmenite"
    molar_mass = 151.73
    density = 4.79
    formula = "FeTiO3"  # FeO.TiO2

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            elements.Iron(),
            elements.Titanium(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen()
        ]
        pass

