from source.abstract.location.controller import controller

class Controller(controller.Controller):
    def __init__(self):
        controller.Controller.__init__(self)
        pass

    def on_loop(self):
        for entity in self.entities:
            entity.on_loop()
        pass

        self.power_grid.on_loop()
