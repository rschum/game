from source.abstract.location.view import view
from source.global_variables.camera import CAMERA

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        pass

    def on_render(self):
        for row in self.get_near_tiles(CAMERA):
            for t in row:
                if t != None:
                    if CAMERA.in_viewport(t):
                        t.on_render()
            
        for entity in self.entities:
            entity.on_render()
        pass
from source.abstract.location.view import view
from source.global_variables.camera import CAMERA

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        pass

    def on_render(self):
        for row in self.get_near_tiles(CAMERA):
            for t in row:
                if t != None:
                    if CAMERA.in_viewport(t):
                        t.on_render()
            
        for entity in self.entities:
            entity.on_render()
        pass
