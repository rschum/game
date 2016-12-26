from source.chemistry.element import elements
from source.chemistry.chemical import chemical


class Diaspore(chemical.Chemical):

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.name = "Diaspore"
        self.mass = 59.99
        self.density = 3.25  # 3.1 - 3.4
        self.elements = [
            elements.Aluminum(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Hydrogen(),
            elements.Hydrogen(),
            elements.Hydrogen()
        ]
        self.formula = "a-AlO(OH)"
        pass


