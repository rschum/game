import math
import pygame
from source.abstract.base_object.model import model

class MoveState():
    STAND = 0

class Model(model.Model):
    name            = "Entity"
    direction       = 0
    move_state      = MoveState.STAND
    mass            = 0 # in kg
    material        = None
    element_masses  = None

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.position = pygame.math.Vector3(0, 0, 0)
        pass

    def translate(self):
        model.Model.translate(self)
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

    def get_planet(self):
        return self.parent.get_planet()

    def get_kilometer(self):
        return self.parent.get_kilometer()

    def get_hectare(self):
        return parent.get_hectare()

    def get_tile(self):
        return self.parent.get_tile()

    def get_mass(self):
        return self.mass

    def set_mass(self, mass):
        self.mass = mass
        pass

    def get_material(self):
        return self.material

    def set_material(self, material):
        self.material = material
        pass

    def get_element_masses(self):
        if self.element_masses == None:
            element_masses = dict()
            for component in self.material.composition:
                portion = component[0]
                chemical = component[1]
                kmoles = portion * self.mass / chemical.molar_mass

                for element in chemical.elements:
                    element_kg = kmoles * element.mass
                    if element_masses.has_key(element.name):
                        element_masses[element.name] += element_kg
                    else:
                        element_masses[element.name] = element_kg
            self.element_masses = element_masses
        return self.element_masses
