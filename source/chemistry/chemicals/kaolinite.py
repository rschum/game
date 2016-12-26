from source.chemistry.element import elements
from source.chemistry.chemical import chemical


# Al2Si2O5(OH)4 in mineralogy or Al2O3-2SiO2-2H2O in ceramics
class Kaolinite(chemical.Chemical):

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.name = "Kaolinite"
        self.mass = 258.18
        self.density = 2.68  # 2.16 - 2.68
        self.elements = [
            elements.Aluminum(),
            elements.Aluminum(),
            elements.Silicon(),
            elements.Silicon(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Hydrogen(),
            elements.Hydrogen(),
            elements.Hydrogen(),
            elements.Hydrogen(),
        ]
        self.formula = "Al2Si2O5(OH)4"
        pass

# Al2Si2O5(OH)4
