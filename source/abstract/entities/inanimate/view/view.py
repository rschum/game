from source.abstract.entities.entity.view import view
from ..model import model

class View(view.View):
    def __init__(self):
        view.View.__init__(self)

        self.height = 32
        self.width = 32
        pass

    def pretty_print(self, i = 0):
        name = model.Model.name
        print("\033[94m" + "Building a " + name + ".\033[0m")
        pass
