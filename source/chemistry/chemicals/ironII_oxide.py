from source.chemistry import elements
from source.chemistry.chemical import chemical


# FeO
class IronIIOxide(chemical.Chemical):
    name = "IronII Oxide"
    mass = 71.85
    density = 5.75

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            elements.Iron(),
            elements.Oxygen()
        ]
        pass
