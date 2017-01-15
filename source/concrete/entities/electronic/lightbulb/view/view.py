from animation_config import on, off
from source.abstract.entities.electronic.view import view
from source.library.action import action
from ..model import model


class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.dimensions.x = 58
        self.dimensions.y = 100
        self.animation = action.Action(self, off.data)
        pass

    def on_render(self):
        if self.grid.get_charge() >= 50:
            if self.use_state != model.UseState.ON:
                self.use_state = model.UseState.ON
                self.animation = action.Action(self, on.data)
        else:
            if self.use_state != model.UseState.OFF:
                self.use_state = model.UseState.OFF
                self.animation = action.Action(self, off.data)
        
        self.animation.on_render(self)
        pass

