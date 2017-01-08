from source.abstract.entities.inanimate.view import view
from source.library.action import action

from ..model import model

from animation_config import percent_000, percent_020, percent_040, percent_060, percent_080, percent_100

class View(view.View):
    height  = 64
    width   = 32
    
    def __init__(self):
        view.View.__init__(self)
        self.animation = action.Action(percent_000.data)
        pass

    def on_render(self):
        if self.charge < 19:
            if self.charge_state != model.ChargeState.PERCENT_000:
                self.charge_state = model.ChargeState.PERCENT_000
                self.animation = action.Action(percent_000.data)
        if self.charge >= 20 and self.charge <= 39:
            if self.charge_state != model.ChargeState.PERCENT_020:
                self.charge_state = model.ChargeState.PERCENT_020
                self.animation = action.Action(percent_020.data)
        if self.charge >= 40 and self.charge <= 59:
            if self.charge_state != model.ChargeState.PERCENT_040:
                self.charge_state = model.ChargeState.PERCENT_040
                self.animation = action.Action(percent_040.data)
        if self.charge >= 60 and self.charge <= 79:
            if self.charge_state != model.ChargeState.PERCENT_060:
                self.charge_state = model.ChargeState.PERCENT_060
                self.animation = action.Action(percent_060.data)
        if self.charge >= 80 and self.charge <= 99:
            if self.charge_state != model.ChargeState.PERCENT_080:
                self.charge_state = model.ChargeState.PERCENT_080
                self.animation = action.Action(percent_080.data)
        if self.charge >= 100:
            if self.charge_state != model.ChargeState.PERCENT_100:
                self.charge_state = model.ChargeState.PERCENT_100
                self.animation = action.Action(percent_100.data)
        
        self.animation.on_render(self)
        pass

