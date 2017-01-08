from source.abstract.entities.inanimate.view import view
from source.library.action import action

from ..model import model

from animation_config import on, off

class View(view.View):
    height  = 100
    width   = 58

    def __init__(self):
        view.View.__init__(self)
        self.animation = action.Action(off.data)
        pass

    def on_render(self):
        if self.parent.battery0.charge >= 50:
            if self.use_state != model.UseState.ON:
                self.use_state = model.UseState.ON
                self.animation = action.Action(on.data)
        else:
            if self.use_state != model.UseState.OFF:
                self.use_state = model.UseState.OFF
                self.animation = action.Action(off.data)
        
        self.animation.on_render(self)
        pass

