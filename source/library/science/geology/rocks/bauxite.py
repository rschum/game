from source.library.science.chemistry.chemicals import anatase, boehmite, calcium_oxide, diaspore, goethite, gibbsite
from source.library.science.chemistry.chemicals import hematite, ilmenite, kaolinite, silica, water
from source.abstract.chemistry.rock import rock


# this material is loosely based on Wikipedia's description of bauxite
class Bauxite(rock.Rock):

    def __init__(self):
        rock.Rock.__init__(self)
        self.name = "Bauxite"
        self.composition = [
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
        ]
        self.density = 2.3  # this magic number should be calculated as the weighted average of composition's densities.
        pass
