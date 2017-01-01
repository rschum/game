from source.abstract.location.view import view

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        pass

    def on_render(self):
        self.galaxy.on_render()
