from source.abstract.entities.inanimate.view import view
from source.library.action import action

from ..model import model

from animation_config import healthy_seed, healthy_sprout, healthy_ripe
from animation_config import damaged_seed, damaged_sprout, damaged_ripe

class View(view.View):
    height  = 32
    width   = 32
    
    def __init__(self):
        view.View.__init__(self)
        self.animation = action.Action(healthy_seed.data)
        pass

    def on_render(self):
        if self.health_state == model.HealthState.HEALTHY:
            if self.created_delta() <= 10:
                if self.growth_state != model.GrowthState.SEED:
                    self.growth_state = model.GrowthState.SEED
                    self.animation = action.Action(healthy_seed.data)
            elif self.created_delta() <= 20:
                if self.growth_state != model.GrowthState.SPROUT:
                    self.growth_state = model.GrowthState.SPROUT
                    self.animation = action.Action(healthy_sprout.data)
            elif self.created_delta() > 20:
                if self.growth_state != model.GrowthState.RIPE:
                    self.growth_state = model.GrowthState.RIPE
                    self.animation = action.Action(healthy_ripe.data)
        
        if self.health_state == model.HealthState.DAMAGED:
            if self.created_delta() <= 10:
                if self.growth_state != model.GrowthState.SEED:
                    self.growth_state = model.GrowthState.SEED
                    self.animation = action.Action(damaged_seed.data)
            elif self.created_delta() <= 20:
                if self.growth_state != model.GrowthState.SPROUT:
                    self.growth_state = model.GrowthState.SPROUT
                    self.animation = action.Action(damaged_sprout.data)
            elif self.created_delta() > 20:
                if self.growth_state != model.GrowthState.RIPE:
                    self.growth_state = model.GrowthState.RIPE
                    self.animation = action.Action(damaged_ripe.data)
        
        self.animation.on_render(self)
        pass

