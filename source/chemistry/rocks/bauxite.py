from source.chemistry.chemicals import anatase, boehmite, calcium_oxide, diaspore, goethite, gibbsite
from source.chemistry.chemicals import hematite, ilmenite, kaolinite, silica, water
from source.chemistry.composition import composition
from source.abstract.chemistry.rock import rock


class Bauxite(rock.Rock):

    def __init__(self):
        rock.Rock.__init__(self)
        self.name = "Bauxite"
        self.composition = composition.Composition([
            # weathered aluminum variants
            (0.154, boehmite.Boehmite()),
            (0.077, diaspore.Diaspore()),
            (0.385, gibbsite.Gibbsite()),

            # weathered iron variants
            (0.115, goethite.Goethite()),
            (0.115, hematite.Hematite()),

            # others
            (0.058, kaolinite.Kaolinite()),
            (0.029, silica.Silica()),
            (0.023, calcium_oxide.Calcium_oxide()),
            (0.017, anatase.Anatase()),
            (0.015, water.Water()),
            (0.012, ilmenite.Ilmenite()),
        ])
        # this composition is loosely based on Wikipedia's description of bauxite
