from source.library.science.chemistry.element import elements
from source.abstract.chemistry.chemical import chemical


class Diaspore(chemical.Chemical):
    name = "Diaspore"
    molar_mass = 59.99
    density = 3.25  # 3.1 - 3.4
    formula = "a-AlO(OH)"

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            elements.Aluminum(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Hydrogen(),
            elements.Hydrogen(),
            elements.Hydrogen()
        ]
        pass


