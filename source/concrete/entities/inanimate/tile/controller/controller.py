from source.abstract.entities.inanimate.controller import controller

class Controller(controller.Controller):
    is_loopable     = False
    is_collidable   = False
    
    def __init__(self):
        controller.Controller.__init__(self)
        pass
