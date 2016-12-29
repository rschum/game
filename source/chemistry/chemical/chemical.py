class Chemical:
    name        = None         # in Title Case
    molar_mass  = None         # in g/mol
    density     = None      # in g/ml
    elements    = [None]
    formula     = None      # String

    def __init__(self):
        pass

    def pretty_print(self, i=0):
        print(("\t"*i) + self.name)
        for element in self.elements:
            element.pretty_print(i+1)

    def g_from_moles(self, moles):
        return self.molar_mass * moles

    def g_from_ml(self, volume):
        return self.density / volume

    def moles_from_g(self, g):
        return g / self.molar_mass

    def moles_from_ml(self, ml):
        return (ml * self.density) / self.molar_mass

    def moles_from_m3(self, m3):
        ml = m3 * 1e6
        return self.moles_from_ml(ml)

    def ml_from_g(self, g):
        return g / self.density

    def ml_from_moles(self, moles):
        return (moles * self.molar_mass) / self.density
