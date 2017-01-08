from source.abstract.entities.animate.view import view

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.dimensions.x = 32
        self.dimensions.y = 74
        pass

    def get_render_offset(self):
        self.render_offset.x = -(self.dimensions.x / 2)
        self.render_offset.y = -(self.dimensions.y)
        return self.render_offset
