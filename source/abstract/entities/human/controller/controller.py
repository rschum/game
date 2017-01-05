from source.abstract.entities.animate.controller import controller

class Controller(controller.Controller):
    def __init__(self):
        controller.Controller.__init__(self)
        pass

    def on_loop(self):
        controller.Controller.on_loop(self)
        pass
