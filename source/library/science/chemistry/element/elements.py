from source.abstract.chemistry.element.element import Element

# more values can be found at
# http://periodictable.com/index.html

"""
Molar Mass (g/mol) is rounded to two decimal points for three reasons.
1. This is > 0.1% precision - plenty for checking the molar self.molar_mass of compounds.
2. Molar self.masses are only non-integers because they are the weighted average of the isotopes present on Earth.
The sources of meteorites are determined by noting that their isotope composition is different than Earth's. So these
values are probably not all that accurate for Mars.
3. In many cases, 2 decimal places is all that anyone has bothered to measure.
"""

# 1
class Hydrogen(Element):
    number  = 1
    name    = "Hydrogen"
    symbol  = "H"
    mass    = 1.01


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0.75,
            "sun"          : 0.75,
            "meteorite"    : 0.024,
            "crust"        : 0.0015,
            "ocean"        : 0.11,
            "human"        : 0.10
        }
        pass


# 2
class Helium(Element):
    number  = 2
    name    = "Helium"
    symbol  = "He"
    mass    = 4.00


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0.23,
            "sun"          : 0.23,
            "meteorite"    : 0.0,
            "crust"        : 5.5e-9,
            "ocean"        : 7.2e-12,
            "human"        : 0.0
        }
        pass


# 3
class Lithium(Element):
    number  = 3
    name    = "Lithium"
    symbol  = "Li"
    mass    = 6.94


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 6e-9,
            "sun"          : 6e-11,
            "meteorite"    : 1.7e-6,
            "crust"        : 1.7e-5,
            "ocean"        : 1.8e-7,
            "human"        : 3e-8
        }
        pass


# 4
class Beryllium(Element):
    number  = 4
    name    = "Beryllium"
    symbol  = "Be"
    mass    = 9.01


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 1e-9,
            "sun"          : 1e-10,
            "meteorite"    : 2.9e-8,
            "crust"        : 1.9e-6,
            "ocean"        : 6e-13,
            "human"        : 4e-10
        }
        pass


# 5
class Boron(Element):
    number  = 5
    name    = "Boron"
    symbol  = "B"
    mass    = 10.81


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 1e-9,
            "sun"          : 2e-9,
            "meteorite"    : 1.6e-6,
            "crust"        : 8.6e-6,
            "ocean"        : 4.4e-6,
            "human"        : 7e-7
        }
        pass


# 6
class Carbon(Element):
    number  = 6
    name    = "Carbon"
    symbol  = "C"
    mass    = 12.01


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 5e-3,
            "sun"          : 3e-3,
            "meteorite"    : 1.5e-2,
            "crust"        : 1.8e-3,
            "ocean"        : 2.8e-5,
            "human"        : 0.23
        }
        pass


# 7
class Nitrogen(Element):
    number  = 7
    name    = "Nitrogen"
    symbol  = "N"
    mass    = 14.01


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 1e-3,
            "sun"          : 1e-3,
            "meteorite"    : 1.4e-3,
            "crust"        : 2e-5,
            "ocean"        : 5e-7,
            "human"        : 2.6e-2
        }
        pass


# 8
class Oxygen(Element):
    number  = 8
    name    = "Oxygen"
    symbol  = "O"
    mass    = 16.00


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 1e-2,
            "sun"          : 9e-3,
            "meteorite"    : 0.40,
            "crust"        : 0.46,
            "ocean"        : 0.86,
            "human"        : 0.61
        }
        pass


# 9
class Fluorine(Element):
    number  = 9
    name    = "Fluorine"
    symbol  = "F"
    mass    = 19.00


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 4e-7,
            "sun"          : 5e-7,
            "meteorite"    : 8.7e-5,
            "crust"        : 5.4e-4,
            "ocean"        : 1.3e-6,
            "human"        : 3.7e-5
        }
        pass


# 10
class Neon(Element):
    number  = 10
    name    = "Neon"
    symbol  = "Ne"
    mass    = 20.18


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 1.3e-3,
            "sun"          : 1e-3,
            "meteorite"    : 0,
            "crust"        : 3e-9,
            "ocean"        : 1.2e-10,
            "human"        : 0
        }
        pass


# 11
class Sodium(Element):
    number  = 11
    name    = "Sodium"
    symbol  = "Na"
    mass    = 22.99


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 2e-5,
            "sun"          : 4e-5,
            "meteorite"    : 5.5e-3,
            "crust"        : 2.3e-2,
            "ocean"        : 1.1e-2,
            "human"        : 1.4e-3
        }
        pass


# 12
class Magnesium(Element):
    number  = 12
    name    = "Magnesium"
    symbol  = "Mg"
    mass    = 24.31


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 6e-4,
            "sun"          : 7e-4,
            "meteorite"    : 1.2e-1,
            "crust"        : 2.9e-2,
            "ocean"        : 1.3e-3,
            "human"        : 2.7e-4
        }
        pass


# 13
class Aluminum(Element):
    number  = 13
    name    = "Aluminum"
    symbol  = "Al"
    mass    = 26.98


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 5e-5,
            "sun"          : 6e-5,
            "meteorite"    : 9.1e-3,
            "crust"        : 8.1e-2,
            "ocean"        : 5e-9,
            "human"        : 9e-7
        }
        pass


# 14
class Silicon(Element):
    number  = 14
    name    = "Silicon"
    symbol  = "Si"
    mass    = 28.09


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 7e-4,
            "sun"          : 9e-4,
            "meteorite"    : 0.14,
            "crust"        : 0.27,
            "ocean"        : 1e-6,
            "human"        : 2.6e-4
        }
        pass


# 15
class Phosphorus(Element):
    number  = 15
    name    = "Phosphorus"
    symbol  = "P"
    mass    = 30.97


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 7e-6,
            "sun"          : 7e-6,
            "meteorite"    : 1.1e-3,
            "crust"        : 9.9e-4,
            "ocean"        : 7e-8,
            "human"        : 1.1e-2
        }
        pass


# 16
class Sulfur(Element):
    number  = 16
    name    = "Sulfur"
    symbol  = "S"
    mass    = 32.07


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 5e-4,
            "sun"          : 4e-4,
            "meteorite"    : 4e-2,
            "crust"        : 4.2e-4,
            "ocean"        : 9.3e-4,
            "human"        : 2e-3
        }
        pass


# 17
class Chlorine(Element):
    number  = 17
    name    = "Chlorine"
    symbol  = "Cl"
    mass    = 35.45


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 1e-6,
            "sun"          : 8e-6,
            "meteorite"    : 3.7e-4,
            "crust"        : 1.7e-4,
            "ocean"        : 2e-2,
            "human"        : 1.2e-3
        }
        pass


# 18
class Argon(Element):
    number  = 18
    name    = "Argon"
    symbol  = "Ar"
    mass    = 39.95


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 2e-4,
            "sun"          : 7e-5,
            "meteorite"    : 0,
            "crust"        : 1.5e-6,
            "ocean"        : 4.5e-7,
            "human"        : 0
        }
        pass


# 19
class Potassium(Element):
    number  = 19
    name    = "Potassium"
    symbol  = "K"
    mass    = 39.10


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 3e-6,
            "sun"          : 4e-6,
            "meteorite"    : 7e-4,
            "crust"        : 1.5e-2,
            "ocean"        : 4.2e-4,
            "human"        : 2e-3
        }
        pass


# 20
class Calcium(Element):
    number  = 20
    name    = "Calcium"
    symbol  = "Ca"
    mass    = 40.08


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 7e-5,
            "sun"          : 7e-5,
            "meteorite"    : 1.1e-2,
            "crust"        : 0.05,
            "ocean"        : 4.2e-6,
            "human"        : 1.4e-2
        }
        pass


# 21
class Scandium(Element):
    number  = 21
    name    = "Scandium"
    symbol  = "Sc"
    mass    = 44.96


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 3e-8,
            "sun"          : 4e-8,
            "meteorite"    : 6.4e-6,
            "crust"        : 2.6e-5,
            "ocean"        : 1.5e-12,
            "human"        : 0
        }
        pass


# 22
class Titanium(Element):
    number  = 22
    name    = "Titanium"
    symbol  = "Ti"
    mass    = 47.87


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 3e-6,
            "sun"          : 4e-6,
            "meteorite"    : 5.4e-4,
            "crust"        : 6.6e-3,
            "ocean"        : 1e-9,
            "human"        : 0
        }
        pass


# 23
class Vanadium(Element):
    number  = 23
    name    = "Vanadium"
    symbol  = "V"
    mass    = 50.94


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 1e-6,
            "sun"          : 4e-7,
            "meteorite"    : 6.1e-5,
            "crust"        : 1.9e-4,
            "ocean"        : 1.5e-9,
            "human"        : 3e-8
        }
        pass


# 24
class Chromium(Element):
    number  = 24
    name    = "Chromium"
    symbol  = "Cr"
    mass    = 52.00


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 1.5e-5,
            "sun"          : 2e-5,
            "meteorite"    : 3e-3,
            "crust"        : 1.4e-4,
            "ocean"        : 6e-10,
            "human"        : 3e-8
        }
        pass


# 25
class Manganese(Element):
    number  = 25
    name    = "Manganese"
    symbol  = "Mn"
    mass    = 54.94


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 8e-6,
            "sun"          : 1e-5,
            "meteorite"    : 2.7e-3,
            "crust"        : 1.1e-3,
            "ocean"        : 2e-9,
            "human"        : 2e-7
        }
        pass


# 26
class Iron(Element):
    number  = 26
    name    = "Iron"
    symbol  = "Fe"
    mass    = 55.85


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 1.1e-3,
            "sun"          : 1e-3,
            "meteorite"    : 2.2e-1,
            "crust"        : 6.3e-2,
            "ocean"        : 3e-9,
            "human"        : 6e-5
        }
        pass


# 27
class Cobalt(Element):
    number  = 27
    name    = "Cobalt"
    symbol  = "Co"
    mass    = 58.93


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 3e-6,
            "sun"          : 4e-6,
            "meteorite"    : 5.9e-4,
            "crust"        : 3e-5,
            "ocean"        : 8e-11,
            "human"        : 2e-8
        }
        pass


# 28
class Nickel(Element):
    number  = 28
    name    = "Nickel"
    symbol  = "Ni"
    mass    = 58.69


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 29
class Copper(Element):
    number  = 29
    name    = "Copper"
    symbol  = "Cu"
    mass    = 63.55


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 30
class Zinc(Element):
    number  = 30
    name    = "Zinc"
    symbol  = "Zn"
    mass    = 65.41


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 31
class Gallium(Element):
    number  = 31
    name    = "Gallium"
    symbol  = "Ga"
    mass    = 69.72


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 32
class Germanium(Element):
    number  = 32
    name    = "Germanium"
    symbol  = "Ge"
    mass    = 72.64


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 33
class Arsenic(Element):
    number  = 33
    name    = "Arsenic"
    symbol  = "As"
    mass    = 74.92


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 34
class Selenium(Element):
    number  = 34
    name    = "Selenium"
    symbol  = "Se"
    mass    = 78.96


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 35
class Bromine(Element):
    number  = 35
    name    = "Bromine"
    symbol  = "Br"
    mass    = 79.90


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 36
class Krypton(Element):
    number  = 36
    name    = "Krypton"
    symbol  = "Kr"
    mass    = 83.80


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 37
class Rubidium(Element):
    number  = 37
    name    = "Rubidium"
    symbol  = "Rb"
    mass    = 85.47


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 38
class Strontium(Element):
    number  = 38
    name    = "Strontium"
    symbol  = "Sr"
    mass    = 87.62


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 39
class Yttrium(Element):
    number  = 39
    name    = "Yttrium"
    symbol  = "Y"
    mass    = 88.91


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 40
class Zirconium(Element):
    number  = 40
    name    = "Zirconium"
    symbol  = "Zr"
    mass    = 91.22


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


#41
class Niobium(Element):
    number  = 41
    name    = "Niobium"
    symbol  = "Nb"
    mass    = 92.91


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


#42
class Molybdenum(Element):
    number  = 42
    name    = "Molybdenum"
    symbol  = "Mo"
    mass    = 95.94


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


#43
class Technetium(Element):
    number  = 43
    name    = "Technetium"
    symbol  = "Tc"
    mass    = 98   # Radioactive. Mass is for the longest lived isotope.


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 44
class Ruthenium(Element):
    number  = 44
    name    = "Ruthenium"
    symbol  = "Ru"
    mass    = 101.07


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 45
class Rhodium(Element):
    number  = 45
    name    = "Rhodium"
    symbol  = "Rh"
    mass    = 102.91


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 46
class Palladium(Element):
    number  = 46
    name    = "Palladium"
    symbol  = "Pd"
    mass    = 106.42


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 47
class Silver(Element):
    number  = 47
    name    = "Silver"
    symbol  = "Ag"
    mass    = 107.87


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 48
class Cadmium(Element):
    number  = 48
    name    = "Cadmium"
    symbol  = "Cd"
    mass    = 112.41


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 49
class Indium(Element):
    number  = 49
    name    = "Indium"
    symbol  = "In"
    mass    = 114.82


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 50
class Tin(Element):
    number  = 50
    name    = "Tin"
    symbol  = "Sn"
    mass    = 118.71


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 51
class Antimony(Element):
    number  = 51
    name    = "Antimony"
    symbol  = "Sb"
    mass    = 121.76


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 52
class Tellurium(Element):
    number  = 52
    name    = "Tellurium"
    symbol  = "Te"
    mass    = 127.6   # Only 1 decimal place was given.


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 53
class Iodine(Element):
    number  = 53
    name    = "Iodine"
    symbol  = "I"
    mass    = 126.90


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 54
class Xenon(Element):
    number  = 54
    name    = "Xenon"
    symbol  = "Xe"
    mass    = 131.29


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 55
class Cesium(Element):
    number  = 55
    name    = "Cesium"
    symbol  = "Cs"
    mass    = 132.91


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 56
class Barium(Element):
    number  = 56
    name    = "Barium"
    symbol  = "Ba"
    mass    = 137.33


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 57
class Lanthanum(Element):
    number  = 57
    name    = "Lanthanum"
    symbol  = "La"
    mass    = 138.91


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 58
class Cerium(Element):
    number  = 58
    name    = "Cerium"
    symbol  = "Ce"
    mass    = 140.12


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 59
class Praseodymium(Element):
    number  = 59
    name    = "Praseodymium"
    symbol  = "Pr"
    mass    = 140.91


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 60
class Neodymium(Element):
    number  = 60
    name    = "Neodymium"
    symbol  = "Nd"
    mass    = 144.24


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 61
class Promethium(Element):
    number  = 61
    name    = "Promethium"
    symbol  = "Pm"
    mass    = 145   # Radioactive. Mass is for the longest lived isotope.


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 62
class Samarium(Element):
    number  = 62
    name    = "Samarium"
    symbol  = "Sm"
    mass    = 150.36


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 63
class Europium(Element):
    number  = 63
    name    = "Europium"
    symbol  = "Eu"
    mass    = 151.96


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 64
class Gadolinium(Element):
    number  = 64
    name    = "Gadolinium"
    symbol  = "Gd"
    mass    = 157.25


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 65
class Terbium(Element):
    number  = 65
    name    = "Terbium"
    symbol  = "Tb"
    mass    = 158.93


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 66
class Dysprosium(Element):
    number  = 66
    name    = "Dysprosium"
    symbol  = "Dy"
    mass    = 162.5   # Only 1 decimal place was given.


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 67
class Holmium(Element):
    number  = 67
    name    = "Holmium"
    symbol  = "Ho"
    mass    = 164.93


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 68
class Erbium(Element):
    number  = 68
    name    = "Erbium"
    symbol  = "Er"
    mass    = 167.26


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 69
class Thulium(Element):
    number  = 69
    name    = "Thulium"
    symbol  = "Tm"
    mass    = 168.93


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 70
class Ytterbium(Element):
    number  = 70
    name    = "Ytterbium"
    symbol  = "Yb"
    mass    = 173.04


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 71
class Lutetium(Element):
    number  = 71
    name    = "Lutetium"
    symbol  = "Lu"
    mass    = 174.97


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 72
class Hafnium(Element):
    number  = 72
    name    = "Hafnium"
    symbol  = "Hf"
    mass    = 178.49


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 73
class Tantalum(Element):
    number  = 73
    name    = "Tantalum"
    symbol  = "Ta"
    mass    = 180.95


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 74
class Tungsten(Element):
    number  = 74
    name    = "Tungsten"
    symbol  = "W"
    mass    = 183.84


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 75
class Rhenium(Element):
    number  = 75
    name    = "Rhenium"
    symbol  = "Re"
    mass    = 186.21


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 76
class Osmium(Element):
    number  = 76
    name    = "Osmium"
    symbol  = "Os"
    mass    = 190.23


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 77
class Iridium(Element):
    number  = 77
    name    = "Iridium"
    symbol  = "Ir"
    mass    = 192.22


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 78
class Platinum(Element):
    number  = 78
    name    = "Platinum"
    symbol  = "Pt"
    mass    = 195.08


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 79
class Gold(Element):
    number  = 79
    name    = "Gold"
    symbol  = "Au"
    mass    = 196.97


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 80
class Mercury(Element):
    number  = 80
    name    = "Mercury"
    symbol  = "Hg"
    mass    = 200.59


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 81
class Thallium(Element):
    number  = 81
    name    = "Thallium"
    symbol  = "Tl"
    mass    = 204.38


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 82
class Lead(Element):
    number  = 82
    name    = "Lead"
    symbol  = "Pb"
    mass    = 207.2   # Only 1 decimal place was given.


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 83
class Bismuth(Element):
    number  = 83
    name    = "Bismuth"
    symbol  = "Bi"
    mass    = 208.98


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 84
class Polonium(Element):
    number  = 84
    name    = "Polonium"
    symbol  = "Po"
    mass    = 209   # Radioactive. Mass is for the longest lived isotope.


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 85
class Astatine(Element):
    number  = 85
    name    = "Astatine"
    symbol  = "At"
    mass    = 210   # Radioactive. Mass is for the longest lived isotope.


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 86
class Radon(Element):
    number  = 86
    name    = "Radon"
    symbol  = "Rn"
    mass    = 222   # Radioactive. Mass is for the longest lived isotope.


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 87
class Francium(Element):
    number  = 87
    name    = "Francium"
    symbol  = "Fr"
    mass    = 223   # Radioactive. Mass is for the longest lived isotope.


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 88
class Radium(Element):
    number  = 88
    name    = "Radium"
    symbol  = "Ra"
    mass    = 226   # Radioactive. Mass is for the longest lived isotope.


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 89
class Actinium(Element):
    number  = 89
    name    = "Actinium"
    symbol  = "Ac"
    mass    = 227   # Radioactive. Mass is for the longest lived isotope.


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0,
            "sun"          : 0,
            "meteorite"    : 0,
            "crust"        : 0,
            "ocean"        : 0,
            "human"        : 0
        }
        pass


# 90
class Thorium(Element):
    number  = 90
    name    = "Thorium"
    symbol  = "Th"
    mass    = 232.04


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 4e-10,
            "sun"          : 3e-10,
            "meteorite"    : 3.9e-8,
            "crust"        : 6e-6,
            "ocean"        : 4e-14,
            "human"        : 0.0
        }
        pass


# 91
class Protactinium(Element):
    number  = 91
    name    = "Protactinium"
    symbol  = "Pa"
    mass    = 231.04


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 0.0,
            "sun"          : 0.0,
            "meteorite"    : 0.0,
            "crust"        : 9.9e-15,
            "ocean"        : 2e-25,
            "human"        : 0.0
        }
        pass


# 92 - This is the last naturally occuring element. The rest are man-made.
class Uranium(Element):
    number  = 92
    name    = "Uranium"
    symbol  = "U"
    mass    = 238.03


    def __init__(self):
        Element.__init__(self)
        self.abundance = {
            "universe"     : 2e-10,
            "sun"          : 1e-9,
            "meteorite"    : 9.8e-9,
            "crust"        : 1.8e-6,
            "ocean"        : 3.3e-9,
            "human"        : 1e-9
        }
        pass


# 93
class Neptunium(Element):
    number  = 93
    name    = "Neptunium"
    symbol  = "Np"
    mass    = 237   # Radioactive. Mass is for the longest lived isotope.


    def __init__(self):
        Element.__init__(self)
        self.abundance = { # abuncances are actually 0 since this element is man made
            "universe"     : 0.0,
            "sun"          : 0.0,
            "meteorite"    : 0.0,
            "crust"        : 0.0,
            "ocean"        : 0.0,
            "human"        : 0.0
        }
        pass


# 94
class Plutonium(Element):
    number  = 94
    name    = "Plutonium"
    symbol  = "Pu"
    mass    = 244   # Radioactive. Mass is for the longest lived isotope.


    def __init__(self):
        Element.__init__(self)
        self.abundance = { # abuncances are actually 0 since this element is man made
            "universe"     : 0.0,
            "sun"          : 0.0,
            "meteorite"    : 0.0,
            "crust"        : 0.0,
            "ocean"        : 0.0,
            "human"        : 0.0
        }
        pass


# 95 - This is included because it's common in smoke detectors
class Americium(Element):
    number  = 95
    name    = "Americium"
    symbol  = "Am"
    mass    = 243   # Radioactive. Mass is for the longest lived isotope.


    def __init__(self):
        Element.__init__(self)
        self.abundance = { # abuncances are actually 0 since this element is man made
            "universe"     : 0.0,
            "sun"          : 0.0,
            "meteorite"    : 0.0,
            "crust"        : 0.0,
            "ocean"        : 0.0,
            "human"        : 0.0
        }
        pass

