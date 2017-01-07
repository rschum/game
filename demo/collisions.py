#! /usr/bin/python2.7

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from source.abstract.location.model import model
from source.concrete.entities.plant.corn import corn
from source.concrete.entities.plant.turnip import turnip

class Collisions(model.Model):
    def __init__(self):
        model.Model.__init__(self)

        plant0 = corn.Corn(self)
        plant1 = turnip.Turnip(self)

        print plant0.radius
        print plant1.radius

        self.add_entity(plant0)
        self.add_entity(plant1)

    def collide(self):
        for entity in self.entities:
            print entity.name
            print entity.get_collisions()

    def move_out_of_collision_range(self):
        print("\nMove Out of Collision Range.")
        self.entities[0].position.x = 64

if __name__ == "__main__":
    collisions = Collisions()
    collisions.collide()
    collisions.move_out_of_collision_range()
    collisions.collide()
