import pygame
from source.abstract.base_object.model import model

class MoveState():
    STAND = 0

class Model(model.Model):
    position    = None
    direction   = 0
    move_state  = MoveState.STAND
    composition = None

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.position = pygame.math.Vector3(0, 0, 0)
        pass

    def transform(self):
        self.translate()
        self.rotate()
        pass

    def translate(self):
        self.position += self.speed()
        pass

    def rotate(self):
        pass

    def speed(self):
        return pygame.math.Vector3(0,0,0)

    def stand(self):
        self.move_state = MoveState.STAND
        pass

    def drop(self):
        self.position = pygame.math.Vector3(
            self.position.x,
            self.position.y,
            self.position.z
        )

    def get_kilometer(self):
        return (
            math.floor(self.position.x / 10000),
            math.floor(self.position.y / 10000)
        )

    def get_hectare(self):
        return (
            math.floor(self.position.x / 1000),
            math.floor(self.position.y / 1000)
        )

    def get_tile(self):
        return (
            math.floor(self.position.x / 100),
            math.floor(self.position.y / 100)
        )

    def get_composition(self):
        return self.composition

    def set_composition(self, composition):
        self.composition = composition
        pass
