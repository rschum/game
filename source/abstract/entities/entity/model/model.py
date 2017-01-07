import pygame
from source.abstract.base_object.model import model
from source.library.science.math.geometry.g3d.sphere import sphere

class MoveState():
    STAND = 0

class Model(model.Model, sphere.Sphere):
    name        = "Entity"
    direction   = 0
    move_state  = MoveState.STAND
    composition = None

    collisions  = []

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        sphere.Sphere.__init__(self)
        self.collisions = []
        self.radius = 1
        self.position = pygame.math.Vector3(0, 0, 0)
        pass

    def translate(self):
        sphere.Sphere.translate(self)
        self.position += self.speed()
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
        pass

    def get_collisions(self):
        for entity in self.parent.entities:
            if entity is not self:
                if self.collide(entity) == True:
                    if entity not in self.collisions:
                        print self.name
                        self.collisions.append(entity)
                        print(self.name+" "+str(self.uuid)+" is colliding with "+entity.name+" "+str(self.uuid))
                        pass
                else:
                    if entity in self.collisions:
                        print self.name
                        #print self.collisions
                        self.collisions.remove(entity)
                        print(self.name+" "+str(self.uuid)+" is ! colliding with "+entity.name+" "+str(self.uuid))
                        pass
        return self.collisions

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
