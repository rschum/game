from source.abstract.entities.inanimate.model import model

class MoveState():
    STAND = 0

class GrowthState():
    SEED    = 0
    SPROUT  = 1
    SAPLING = 2
    MATURE  = 3
    RIPE    = 4

class HealthState():
    HEALTHY = 0
    DAMAGED = 1

class Model(model.Model):
    growth_state    = GrowthState.SEED
    health_state    = HealthState.HEALTHY

    def __init__(self, parent):
        model.Model.__init__(self, parent)
        pass
