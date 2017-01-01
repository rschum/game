import pygame

class Model:
    clock               = None
    frames_per_second   = 30

    universe = None

    def __init__(self, parent = None):
        self.clock = pygame.time.Clock()
        pass
