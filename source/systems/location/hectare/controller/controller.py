from source.abstract.location.controller import controller

class Controller(controller.Controller):
    def __init__(self):
        controller.Controller.__init__(self)
        pass

    def on_loop(self):
        controller.Controller.on_loop(self)
        camera = self.entity_manager.camera
        for row in self.get_near_tiles(camera):
            for t in row:
                if t != None:
                    if camera.in_viewport(t):
                        t.on_loop()
        pass
