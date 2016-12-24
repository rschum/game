from source.chemistry import elements
from source.chemistry.chemical import chemical


# Fe(III)2O3
class Hematite(chemical.Chemical):
    name = "Hematite"
    mass = 159.70
    density = 5.26

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            elements.Iron(),
            elements.Iron(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen()
        ]
        pass
