from source.abstract.location.view import view

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        pass

    def on_render(self):
        for kilometer in self.kilometers:
            for kilo in kilometer:
                kilo.on_render()
        
        view.View.on_render(self)
        pass
