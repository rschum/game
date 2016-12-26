from source.chemistry.element.element import Element

# more values can be found at
# http://periodictable.com/index.html

"""
Molar Mass (g/mol) is rounded to two decimal points for three reasons.
1. This is > 0.1% precision - plenty for checking the molar self.mass of compounds.
2. Molar self.masses are only non-integers because they are the weighted average of the isotopes present on Earth.
The sources of meteorites are determined by noting that their isotope composition is different than Earth's. So these
values are probably not all that accurate for Mars.
3. In many cases, 2 decimal places is all that anyone has bothered to measure.
"""

# 1
class Hydrogen(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 1
        self.name    = "Hydrogen"
        self.symbol  = "H"
        self.mass    = 1.01
        pass


# 2
class Helium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 2
        self.name    = "Helium"
        self.symbol  = "He"
        self.mass    = 4.00
        pass


# 3
class Lithium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 3
        self.name    = "Lithium"
        self.symbol  = "Li"
        self.mass    = 6.94
        pass


# 4
class Beryllium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 4
        self.name    = "Beryllium"
        self.symbol  = "Be"
        self.mass    = 9.01
        pass


# 5
class Boron(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 5
        self.name    = "Boron"
        self.symbol  = "B"
        self.mass    = 10.81
        pass


# 6
class Carbon(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 6
        self.name    = "Carbon"
        self.symbol  = "C"
        self.mass    = 12.01
        pass


# 7
class Nitrogen(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 7
        self.name    = "Nitrogen"
        self.symbol  = "N"
        self.mass    = 14.01
        pass


# 8
class Oxygen(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 8
        self.name    = "Oxygen"
        self.symbol  = "O"
        self.mass    = 16.00
        pass


# 9
class Fluorine(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 9
        self.name    = "Fluorine"
        self.symbol  = "F"
        self.mass    = 19.00
        pass


# 10
class Neon(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 10
        self.name    = "Neon"
        self.symbol  = "Ne"
        self.mass    = 20.18
        pass


# 11
class Sodium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 11
        self.name    = "Sodium"
        self.symbol  = "Na"
        self.mass    = 22.99
        pass


# 12
class Magnesium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 12
        self.name    = "Magnesium"
        self.symbol  = "Mg"
        self.mass    = 24.31
        pass


# 13
class Aluminum(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 13
        self.name    = "Aluminum"
        self.symbol  = "Al"
        self.mass    = 26.98
        pass


# 14
class Silicon(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 14
        self.name    = "Silicon"
        self.symbol  = "Si"
        self.mass    = 28.09
        pass


# 15
class Phosphorus(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 15
        self.name    = "Phosphorus"
        self.symbol  = "P"
        self.mass    = 30.97
        pass


# 16
class Sulfur(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 16
        self.name    = "Sulfur"
        self.symbol  = "S"
        self.mass    = 32.07
        pass


# 17
class Chlorine(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 17
        self.name    = "Chlorine"
        self.symbol  = "Cl"
        self.mass    = 35.45
        pass


# 18
class Argon(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 18
        self.name    = "Argon"
        self.symbol  = "Ar"
        self.mass    = 39.95
        pass


# 19
class Potassium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 19
        self.name    = "Potassium"
        self.symbol  = "K"
        self.mass    = 39.10
        pass


# 20
class Calcium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 20
        self.name    = "Calcium"
        self.symbol  = "Ca"
        self.mass    = 40.08
        pass


# 21
class Scandium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 21
        self.name    = "Scandium"
        self.symbol  = "Sc"
        self.mass    = 44.96
        pass


# 22
class Titanium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 22
        self.name    = "Titanium"
        self.symbol  = "Ti"
        self.mass    = 47.87
        pass


# 23
class Vanadium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 23
        self.name    = "Vanadium"
        self.symbol  = "V"
        self.mass    = 50.94
        pass


# 24
class Chromium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 24
        self.name    = "Chromium"
        self.symbol  = "Cr"
        self.mass    = 52.00
        pass


# 25
class Manganese(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 25
        self.name    = "Manganese"
        self.symbol  = "Mn"
        self.mass    = 54.94
        pass


# 26
class Iron(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 26
        self.name    = "Iron"
        self.symbol  = "Fe"
        self.mass    = 55.85
        pass


# 27
class Cobalt(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 27
        self.name    = "Cobalt"
        self.symbol  = "Co"
        self.mass    = 58.93
        pass


# 28
class Nickel(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 28
        self.name    = "Nickel"
        self.symbol  = "Ni"
        self.mass    = 58.69
        pass


# 29
class Copper(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 29
        self.name    = "Copper"
        self.symbol  = "Cu"
        self.mass    = 63.55
        pass


# 30
class Zinc(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 30
        self.name    = "Zinc"
        self.symbol  = "Zn"
        self.mass    = 65.41
        pass


# 31
class Gallium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 31
        self.name    = "Gallium"
        self.symbol  = "Ga"
        self.mass    = 69.72
        pass


# 32
class Germanium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 32
        self.name    = "Germanium"
        self.symbol  = "Ge"
        self.mass    = 72.64
        pass


# 33
class Arsenic(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 33
        self.name    = "Arsenic"
        self.symbol  = "As"
        self.mass    = 74.92
        pass


# 34
class Selenium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 34
        self.name    = "Selenium"
        self.symbol  = "Se"
        self.mass    = 78.96
        pass


# 35
class Bromine(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 35
        self.name    = "Bromine"
        self.symbol  = "Br"
        self.mass    = 79.90
        pass


# 36
class Krypton(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 36
        self.name    = "Krypton"
        self.symbol  = "Kr"
        self.mass    = 83.80
        pass


# 37
class Rubidium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 37
        self.name    = "Rubidium"
        self.symbol  = "Rb"
        self.mass    = 85.47
        pass


# 38
class Strontium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 38
        self.name    = "Strontium"
        self.symbol  = "Sr"
        self.mass    = 87.62
        pass


# 39
class Yttrium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 39
        self.name    = "Yttrium"
        self.symbol  = "Y"
        self.mass    = 88.91
        pass


# 40
class Zirconium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 40
        self.name    = "Zirconium"
        self.symbol  = "Zr"
        self.mass    = 91.22
        pass


#41
class Niobium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 41
        self.name    = "Niobium"
        self.symbol  = "Nb"
        self.mass    = 92.91
        pass


#42
class Molybdenum(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 42
        self.name    = "Molybdenum"
        self.symbol  = "Mo"
        self.mass    = 95.94
        pass


#43
class Technetium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 43
        self.name    = "Technetium"
        self.symbol  = "Tc"
        self.mass    = 98   # Radioactive. Mass is for the longest lived isotope.
        pass


# 44
class Ruthenium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 44
        self.name    = "Ruthenium"
        self.symbol  = "Ru"
        self.mass    = 101.07
        pass


# 45
class Rhodium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 45
        self.name    = "Rhodium"
        self.symbol  = "Rh"
        self.mass    = 102.91
        pass


# 46
class Palladium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 46
        self.name    = "Palladium"
        self.symbol  = "Pd"
        self.mass    = 106.42
        pass


# 47
class Silver(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 47
        self.name    = "Silver"
        self.symbol  = "Ag"
        self.mass    = 107.87
        pass


# 48
class Cadmium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 48
        self.name    = "Cadmium"
        self.symbol  = "Cd"
        self.mass    = 112.41
        pass


# 49
class Indium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 49
        self.name    = "Indium"
        self.symbol  = "In"
        self.mass    = 114.82
        pass


# 50
class Tin(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 50
        self.name    = "Tin"
        self.symbol  = "Sn"
        self.mass    = 118.71
        pass


# 51
class Antimony(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 51
        self.name    = "Antimony"
        self.symbol  = "Sb"
        self.mass    = 121.76
        pass


# 52
class Tellurium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 52
        self.name    = "Tellurium"
        self.symbol  = "Te"
        self.mass    = 127.6   # Only 1 decimal place was given.
        pass


# 53
class Iodine(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 53
        self.name    = "Iodine"
        self.symbol  = "I"
        self.mass    = 126.90
        pass


# 54
class Xenon(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 54
        self.name    = "Xenon"
        self.symbol  = "Xe"
        self.mass    = 131.29
        pass


# 55
class Cesium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 55
        self.name    = "Cesium"
        self.symbol  = "Cs"
        self.mass    = 132.91
        pass


# 56
class Barium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 56
        self.name    = "Barium"
        self.symbol  = "Ba"
        self.mass    = 137.33
        pass


# 57
class Lanthanum(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 57
        self.name    = "Lanthanum"
        self.symbol  = "La"
        self.mass    = 138.91
        pass


# 58
class Cerium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 58
        self.name    = "Cerium"
        self.symbol  = "Ce"
        self.mass    = 140.12
        pass


# 59
class Praseodymium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 59
        self.name    = "Praseodymium"
        self.symbol  = "Pr"
        self.mass    = 140.91
        pass


# 60
class Neodymium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 60
        self.name    = "Neodymium"
        self.symbol  = "Nd"
        self.mass    = 144.24
        pass


# 61
class Promethium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 61
        self.name    = "Promethium"
        self.symbol  = "Pm"
        self.mass    = 145   # Radioactive. Mass is for the longest lived isotope.
        pass


# 62
class Samarium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 62
        self.name    = "Samarium"
        self.symbol  = "Sm"
        self.mass    = 150.36
        pass


# 63
class Europium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 63
        self.name    = "Europium"
        self.symbol  = "Eu"
        self.mass    = 151.96
        pass


# 64
class Gadolinium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 64
        self.name    = "Gadolinium"
        self.symbol  = "Gd"
        self.mass    = 157.25
        pass


# 65
class Terbium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 65
        self.name    = "Terbium"
        self.symbol  = "Tb"
        self.mass    = 158.93
        pass


# 66
class Dysprosium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 66
        self.name    = "Dysprosium"
        self.symbol  = "Dy"
        self.mass    = 162.5   # Only 1 decimal place was given.
        pass


# 67
class Holmium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 67
        self.name    = "Holmium"
        self.symbol  = "Ho"
        self.mass    = 164.93
        pass


# 68
class Erbium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 68
        self.name    = "Erbium"
        self.symbol  = "Er"
        self.mass    = 167.26
        pass


# 69
class Thulium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 69
        self.name    = "Thulium"
        self.symbol  = "Tm"
        self.mass    = 168.93
        pass


# 70
class Ytterbium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 70
        self.name    = "Ytterbium"
        self.symbol  = "Yb"
        self.mass    = 173.04
        pass


# 71
class Lutetium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 71
        self.name    = "Lutetium"
        self.symbol  = "Lu"
        self.mass    = 174.97
        pass


# 72
class Hafnium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 72
        self.name    = "Hafnium"
        self.symbol  = "Hf"
        self.mass    = 178.49
        pass


# 73
class Tantalum(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 73
        self.name    = "Tantalum"
        self.symbol  = "Ta"
        self.mass    = 180.95
        pass


# 74
class Tungsten(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 74
        self.name    = "Tungsten"
        self.symbol  = "W"
        self.mass    = 183.84
        pass


# 75
class Rhenium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 75
        self.name    = "Rhenium"
        self.symbol  = "Re"
        self.mass    = 186.21
        pass


# 76
class Osmium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 76
        self.name    = "Osmium"
        self.symbol  = "Os"
        self.mass    = 190.23
        pass


# 77
class Iridium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 77
        self.name    = "Iridium"
        self.symbol  = "Ir"
        self.mass    = 192.22
        pass


# 78
class Platinum(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 78
        self.name    = "Platinum"
        self.symbol  = "Pt"
        self.mass    = 195.08
        pass


# 79
class Gold(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 79
        self.name    = "Gold"
        self.symbol  = "Au"
        self.mass    = 196.97
        pass


# 80
class Mercury(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 80
        self.name    = "Mercury"
        self.symbol  = "Hg"
        self.mass    = 200.59
        pass


# 81
class Thallium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 81
        self.name    = "Thallium"
        self.symbol  = "Tl"
        self.mass    = 204.38
        pass


# 82
class Lead(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 82
        self.name    = "Lead"
        self.symbol  = "Pb"
        self.mass    = 207.2   # Only 1 decimal place was given.
        pass


# 83
class Bismuth(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 83
        self.name    = "Bismuth"
        self.symbol  = "Bi"
        self.mass    = 208.98
        pass


# 84
class Polonium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 84
        self.name    = "Polonium"
        self.symbol  = "Po"
        self.mass    = 209   # Radioactive. Mass is for the longest lived isotope.
        pass


# 85
class Astatine(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 85
        self.name    = "Astatine"
        self.symbol  = "At"
        self.mass    = 210   # Radioactive. Mass is for the longest lived isotope.
        pass


# 86
class Radon(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 86
        self.name    = "Radon"
        self.symbol  = "Rn"
        self.mass    = 222   # Radioactive. Mass is for the longest lived isotope.
        pass


# 87
class Francium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 87
        self.name    = "Francium"
        self.symbol  = "Fr"
        self.mass    = 223   # Radioactive. Mass is for the longest lived isotope.
        pass


# 88
class Radium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 88
        self.name    = "Radium"
        self.symbol  = "Ra"
        self.mass    = 226   # Radioactive. Mass is for the longest lived isotope.
        pass


# 89
class Actinium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 89
        self.name    = "Actinium"
        self.symbol  = "Ac"
        self.mass    = 227   # Radioactive. Mass is for the longest lived isotope.
        pass


# 90
class Thorium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 90
        self.name    = "Thorium"
        self.symbol  = "Th"
        self.mass    = 232.04
        pass


# 91
class Protactinium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 91
        self.name    = "Protactinium"
        self.symbol  = "Pa"
        self.mass    = 231.04
        pass


# 92 - This is the last naturally occuring element. The rest are man-made.
class Uranium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 92
        self.name    = "Uranium"
        self.symbol  = "U"
        self.mass    = 238.03
        pass


# 93
class Neptunium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 93
        self.name    = "Neptunium"
        self.symbol  = "Np"
        self.mass    = 237   # Radioactive. Mass is for the longest lived isotope.
        pass


# 94
class Plutonium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 94
        self.name    = "Plutonium"
        self.symbol  = "Pu"
        self.mass    = 244   # Radioactive. Mass is for the longest lived isotope.
        pass


# 95 - This is included because it's common in smoke detectors
class Americium(Element):
    def __init__(self):
        Element.__init__(self)
        self.number  = 95
        self.name    = "Americium"
        self.symbol  = "Am"
        self.mass    = 243   # Radioactive. Mass is for the longest lived isotope.
        pass

