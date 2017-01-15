from source.abstract.base_object.model import model

import pygame

class Model(model.Model):
    clock               = None
    frames_per_second   = 30

    def __init__(self, parent = None):
        model.Model.__init__(self)
        self.clock = pygame.time.Clock()
        pass
