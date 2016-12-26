from source.chemistry.element import elements
from source.chemistry.chemical import chemical


class Boehmite(chemical.Chemical):

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.name = "Boehmite"
        self.mass = 59.99
        self.density = 3.03  # 3.02 - 3.05
        self.elements = [
            elements.Aluminum(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Hydrogen(),
        ]
        self.formula = "g-AlO(OH)"
        pass

