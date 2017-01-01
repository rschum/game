from source.chemistry.element import elements
from source.chemistry.chemical import chemical


class Goethite(chemical.Chemical):
    name = "Goethite"
    molar_mass = 88.86
    density = 4.0  # 3.3 - 4.3
    formula = "FeO(OH)"

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            elements.Iron(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Hydrogen(),
        ]
        pass
