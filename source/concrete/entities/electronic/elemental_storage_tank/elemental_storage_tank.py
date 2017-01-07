from controller import controller
from model import model
from view import view

class ElementalStorageTank(controller.Controller, model.Model, view.View):
    def __init__(self, parent, element, capacity):
        controller.Controller.__init__(self)
        model.Model.__init__(self, parent, element, capacity)
        view.View.__init__(self)
        pass
