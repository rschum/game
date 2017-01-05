#! /usr/bin/python2.7

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from source.systems.game import game

if __name__ == "__main__":
    game = game.Game()
    game.on_loop()
