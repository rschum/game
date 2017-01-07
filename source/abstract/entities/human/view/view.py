from source.abstract.entities.animate.view import view

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.height = 74
        self.width = 32
        self.render_offset.x = -(self.width / 2)
        self.render_offset.y = -(self.height)
        pass
