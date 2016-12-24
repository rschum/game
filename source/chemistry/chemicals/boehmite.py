from source.chemistry import elements
from source.chemistry.chemical import chemical


# gamma-AlO(OH)
class Boehmite(chemical.Chemical):
    name = "Boehmite"
    mass = 59.99
    density = 3.03  # 3.02 - 3.05

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            elements.Aluminum(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Hydrogen()
        ]
        pass

