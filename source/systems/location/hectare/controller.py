from source.abstract.location.controller import controller

class Controller(controller.Controller):
    def __init__(self):
        controller.Controller.__init__(self)
        pass

    def on_loop(self, obj):
        for row in self.get_near_tiles(obj):
            for t in row:
                if t != None:
                    t.on_loop()
        
        for entity in self.entities:
            entity.on_loop()
        pass
