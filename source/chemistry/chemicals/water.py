from source.chemistry.element import elements
from source.chemistry.chemical import chemical


class Water(chemical.Chemical):
    name = "Water"
    mass = 18.02
    density = 1.00
    elements = [
        elements.Oxygen(),
        elements.Hydrogen(),
        elements.Hydrogen(),
    ]
    formula = "H2O"

    def __init__(self):
        chemical.Chemical.__init__(self)
        pass
