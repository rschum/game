from source.library.science.chemistry.element import elements
from source.abstract.chemistry.chemical import chemical


class Boehmite(chemical.Chemical):
    name = "Boehmite"
    molar_mass = 59.99
    density = 3.03  # 3.02 - 3.05
    formula = "g-AlO(OH)"

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            elements.Aluminum(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Hydrogen(),
        ]
        pass

