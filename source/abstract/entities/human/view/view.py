from source.abstract.entities.animate.view import view

class View(view.View):
    height  = 74
    width   = 32
    
    def __init__(self):
        view.View.__init__(self)
        pass

    def get_render_offset(self):
        self.render_offset.x = -(self.width / 2)
        self.render_offset.y = -(self.height)
        return self.render_offset
