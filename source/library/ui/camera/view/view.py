from source.abstract.entities.entity.view import view

import pygame
from source.global_variables import global_variables

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.dimensions = pygame.math.Vector3(
            global_variables.RESOLUTION_X,
            global_variables.RESOLUTION_Y,
            global_variables.RESOLUTION_Z
        )
        pass
