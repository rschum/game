from source.chemistry.element import elements
from source.chemistry.chemical import chemical


# Al(OH)3
class Gibbsite(chemical.Chemical):

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.name = "Gibbsite"
        self.mass = 78.01
        self.density = 2.35
        self.elements = [
            elements.Aluminum(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Hydrogen(),
            elements.Hydrogen(),
            elements.Hydrogen(),
        ]
        self.formula = "Al(OH)3"
        pass
