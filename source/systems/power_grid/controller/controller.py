from source.abstract.location.controller import controller

class Controller(controller.Controller):
    def __init__(self):
        controller.Controller.__init__(self)
        pass

    def on_loop(self):
        self.charge()

        for drain in self.drains:
            drain.discharge()
        pass
