from source.abstract.location.view import view

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        pass

    def on_render(self):
        camera = self.entity_factory.camera
        for row in self.get_near_tiles(camera):
            for t in row:
                if t != None:
                    if camera.in_viewport(t):
                        t.on_render()
                        pass
        
        #view.View.on_render(self)
        pass
