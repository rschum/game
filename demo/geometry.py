#! /usr/bin/python2.7

from pygame import math

def collide(object_0, object_1):
    distance = object_0.position.distance_to(object_1.position)
    if distance < object_0.radius + object_1.radius:
        print "collide"
    else:
        print "not collide"

class Sphere:
    position    = None
    radius      = 1

    def __init__(self):
        self.position = math.Vector3(0, 0, 0)
        pass

    def get_nodes(self):
        return None

    def collide(self, object):
        distance = self.position.distance_to(object.position)
        if distance < self.radius + object.radius:
            return True
        else:
            return False

if __name__ == "__main__":
    sphere_0 = Sphere()
    sphere_1 = Sphere()
    
    sphere_0.position.y = -1
    sphere_0.position.z = -1
    
    print sphere_0.collide(sphere_1)

class Cube:
    position    = None
    width       = 1
    length      = 1
    height      = 1
    nodes       = []

    def __init__(self):
        self.position = math.Vector3(0, 0, 0)
        pass

    def get_nodes(self):
        cube_nodes = [
            (x,y,z) for x in (
                0 + self.position.x,
                self.width + self.position.x
            ) for y in (
                0  + self.position.y,
                self.length + self.position.y
            ) for z in (
                0  + self.position.z,
                self.height + self.position.z
            )
        ]
        return cube_nodes
