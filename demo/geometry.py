#! /usr/bin/python2.7

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from source.library.science.math.geometry.g3d.sphere import sphere
from source.library.science.math.geometry.g3d.cube import cube

if __name__ == "__main__":
    sphere_0 = sphere.Sphere()
    sphere_1 = sphere.Sphere()
    
    sphere_0.position.y = 2
    sphere_0.position.z = -1
    
    print sphere_0.collide(sphere_1)

    cube = cube.Cube()
    print cube.get_nodes()
