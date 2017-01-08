from source.abstract.entities.inanimate.view import view
from source.library.action import action

from animation_config import stand, mined

class View(view.View):
    draw_radius = False
    
    def __init__(self):
        view.View.__init__(self)
        self.dimensions.x = 100
        self.dimensions.y = 100
        self.animation = action.Action(stand.data)
        pass

    def get_render_offset(self):
        self.render_offset.x = 0
        self.render_offset.y = 0
        return self.render_offset


    def on_render(self):
        if self.mined == False:
            if self.animation == None or self.animation.action != "stand":
                self.animation = action.Action(stand.data)
        if self.mined == True:
            if self.animation == None or self.animation.action != "mined":
                self.animation = action.Action(mined.data)
        self.animation.on_render(self)
        pass

