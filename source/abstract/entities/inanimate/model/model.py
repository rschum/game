from source.abstract.entities.entity.model import model

class MoveState():
    STAND = 0

class Model(model.Model):
    name    = "InanimateEntity"
    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        pass
