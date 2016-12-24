from source.chemistry import elements
from source.chemistry.chemical import chemical


# Al(OH)3
class Gibbsite(chemical.Chemical):
    name = "Gibbsite"
    mass = 78.01
    density = 2.35

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
