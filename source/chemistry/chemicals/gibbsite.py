from source.chemistry.element import elements
from source.abstract.chemistry.chemical import chemical


# Al(OH)3
class Gibbsite(chemical.Chemical):
    name = "Gibbsite"
    molar_mass = 78.01
    density = 2.35
    formula = "Al(OH)3"

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            elements.Aluminum(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Hydrogen(),
            elements.Hydrogen(),
            elements.Hydrogen(),
        ]
        pass
