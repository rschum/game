from source.abstract.entities.inanimate.view import view
from source.library.action import action

from animation_config import percent_000, percent_020, percent_040, percent_060, percent_080, percent_100

from ..model import model

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.animation = action.Action(percent_000.percent_000_data)
        self.height = 32
        self.width = 32
        pass

    def on_render(self):
        p = self.get_stored_percent()
        if p < .19:
            if self.capacity_state != model.CapacityState.PERCENT_000:
                self.capacity_state = self.model.CapacityState.PERCENT_000
                self.animation = action.Action(percent_000.percent_000_data)
        if p >= .20 and p <= .39:
            if self.capacity_state != model.CapacityState.PERCENT_020:
                self.capacity_state = model.CapacityState.PERCENT_020
                self.animation = action.Action(percent_020.percent_020_data)
        if p >= .40 and p <= .59:
            if self.capacity_state != model.CapacityState.PERCENT_040:
                self.capacity_state = model.CapacityState.PERCENT_040
                self.animation = action.Action(percent_040.percent_040_data)
        if p >= .60 and p <= .79:
            if self.capacity_state != model.CapacityState.PERCENT_060:
                self.capacity_state = model.CapacityState.PERCENT_060
                self.animation = action.Action(percent_060.percent_060_data)
        if p >= .80 and p <= .99:
            if self.capacity_state != model.CapacityState.PERCENT_080:
                self.capacity_state = model.CapacityState.PERCENT_080
                self.animation = action.Action(percent_080.percent_080_data)
        if p >= .100:
            if self.capacity_state != model.CapacityState.PERCENT_100:
                self.capacity_state = model.CapacityState.PERCENT_100
                self.animation = action.Action(percent_100.percent_100_data)
        self.animation.on_render(self)
        pass

    def pretty_print(self, i=0):
        print(("\t"*i)+self.element+" "+str(self.stored)+"/"+str(self.get_stored_percent()))
