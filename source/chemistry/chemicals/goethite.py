from source.chemistry.element import elements
from source.chemistry.chemical import chemical


class Goethite(chemical.Chemical):

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.name = "Goethite"
        self.mass = 88.86
        self.density = 4.0  # 3.3 - 4.3
        self.elements = [
            elements.Iron(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Hydrogen(),
        ]
        self.formula = "FeO(OH)"
        pass
