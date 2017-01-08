from source.library.action import action

from source.abstract.entities.inanimate.view import view

from animation_config import stand

class View(view.View):
    height  = 100
    width   = 100
    
    def __init__(self):
        view.View.__init__(self)
        self.animation = action.Action(stand.stand_data)
        pass

    def get_render_offset(self):
        self.render_offset.x = -(self.width / 2)
        self.render_offset.y = -(self.height / 2)
        return self.render_offset

