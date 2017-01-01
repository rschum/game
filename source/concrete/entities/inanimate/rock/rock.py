from controller import controller
from model import model
from view import view

class Rock(controller.Controller, model.Model, view.View):
    def __init__(self, parent = None, volume = 1, composition = None):
        controller.Controller.__init__(self)
        model.Model.__init__(self, parent, volume, composition)
        view.View.__init__(self)
        pass
