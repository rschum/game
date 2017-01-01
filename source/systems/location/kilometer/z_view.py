from source.abstract.location.view import view

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        pass

    def on_render(self):
        for hectare in self.hectares:
            for hect in hectare:
                hect.on_render()
