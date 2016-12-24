from source.chemistry import boehmite
from source.chemistry import goethite, gibbsite, ironII_oxide, hematite, kaolinite
from source.chemistry import mineral


class Bauxite(mineral.Mineral):
    name = "Bauxite"

    def __init__(self):
        mineral.Mineral.__init__(self)
        self.chemicals = [
            goethite.Goethite(),
            gibbsite.Gibbsite(),
            boehmite.Boehmite(),
            ironII_oxide.IronIIOxide(),
            hematite.Hematite(),
            kaolinite.Kaolinite()
        ]
