from source.abstract.entities.inanimate.view import view
from source.library.action import action

from animation_config import stand, mined

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.animation = action.Action(stand.stand_data)
        self.height = 100
        self.width = 100
        pass

    def on_render(self):
        if self.mined == False:
            if self.animation == None or self.animation.action != "stand":
                self.animation = action.Action(stand.stand_data)
        if self.mined == True:
            if self.animation == None or self.animation.action != "mined":
                self.animation = action.Action(mined.mined_data)
        self.animation.on_render(self)
        pass

