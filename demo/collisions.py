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

        #plant1.position.x = 30
        #plant1.position.y = 100

        self.add_entity(plant0)
        self.add_entity(plant1)

    def print_positions(self):
        print self.entities[0].position
        print self.entities[1].position

    def collide(self):
        for entity in self.entities:
            print entity.name
            print entity.get_collisions()

if __name__ == "__main__":
    collisions = Collisions()
    collisions.print_positions()
    collisions.collide()
    collisions.collide()
