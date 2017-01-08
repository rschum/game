from controller import controller
from model import model
from view import view

class ElementalStorageUnit(controller.Controller, model.Model, view.View):
    def __init__(self, parent = None):
        controller.Controller.__init__(self)
        model.Model.__init__(self, parent)
        view.View.__init__(self)
        pass

    def get_render_offset(self):
        self.render_offset.x = -(self.width / 2)
        self.render_offset.y = -(self.height / 2)
        return self.render_offset
