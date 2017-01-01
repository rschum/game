import controller, model, view

class Rock(controller.Controller, model.Model, view.View):
    def __init__(self, parent, volume = 1, composition = None):
        controller.Controller.__init__(self)
        model.Model.__init__(self, parent, volume, composition)
        view.View.__init__(self)
        pass
