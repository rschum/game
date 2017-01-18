from source.concrete.entities.electronic.battery import battery
from source.concrete.entities.electronic.lightbulb import lightbulb
from source.concrete.entities.electronic.refinery import refinery
from source.concrete.entities.electronic.replicator import replicator
from source.concrete.entities.electronic.solar_panel import solar_panel
from source.concrete.entities.human.avatar import avatar
from source.concrete.entities.inanimate.tile import tile
from source.concrete.entities.plant.corn import corn
from source.concrete.entities.plant.potato import potato
from source.concrete.entities.plant.turnip import turnip
from source.concrete.entities.plant.tomato import tomato
from source.systems.location.hectare import hectare
from source.systems.location.homestead import homestead
from source.systems.location.kilometer import kilometer
from source.systems.location.galaxy import galaxy
from source.systems.location.planet import planet
from source.systems.location.solar_system import solar_system
from source.systems.location.universe import universe
from source.systems.logistics import logistics
from source.systems.power_grid import power_grid
from source.library.ui.camera import camera

class Model:
    parent          = None
    universes       = {}
    galaxies        = {}
    solar_systems   = {}
    planets         = {}
    kilometers      = {}
    hectares        = {}
    tiles           = {}
    homesteads      = {}
    logistics       = {}
    power_grids     = {}
    entities        = {}
    avatars         = {}
    cameras         = {}
    layers          = {}
    elements        = {}
    chemicals       = {}
    images          = {}
    frames          = {}
    animations      = {}
    music           = {}
    sound_effects   = {}
    camera          = None

    def __init__(self, parent = None):
        self.parent = parent
        cam = self.spawn(camera.Camera, None)
        uni = self.spawn(universe.Universe, None)
        hom = self.spawn(homestead.Homestead, uni)
        ava = self.spawn(avatar.Avatar, uni)
        cam.set_target(ava)
        pass

    def spawn(self, Entity, parent = None):
        e = Entity(parent)
        e.entity_manager = self
        if(Entity is avatar.Avatar):
            self.avatars[e.uuid] = e
        elif(Entity is camera.Camera):
            self.camera = e
        elif(Entity is galaxy.Galaxy):
            self.galaxies[e.uuid] = e
        elif(Entity is hectare.Hectare):
            self.hectares[e.uuid] = e
        elif(Entity is homestead.Homestead):
            self.homesteads[e.uuid] = e
        elif(Entity is logistics.Logistics):
            self.logistics[e.uuid] = e
        elif(Entity is kilometer.Kilometer):
            self.kilometers[e.uuid] = e
        elif(Entity is planet.Planet):
            self.planets[e.uuid] = e
        elif(Entity is solar_system.SolarSystem):
            self.solar_systems[e.uuid] = e
        elif(Entity is tile.Tile):
            self.tiles[e.uuid] = e
        elif(Entity is power_grid.PowerGrid):
            self.power_grids[e.uuid] = e
        elif(Entity is universe.Universe):
            self.universes[e.uuid] = e
        else:
            self.entities[e.uuid] = e
        e.spawn()
        return e

    def despawn(self, object):
        object.parent.disown_child(object)
        for entity in self.entities:
            if self.entities[entity] is object:
                del self.entities[entity]
                break
        pass

    def get_app(self):
        return self.parent.get_app()

    def find_nearest(self, object, objects = None):
        if objects is None:
            objects = self.entity_manager.entities

        shortest_distance = None
        item = None
        for obj in objects:
            e = objects[obj]
            distance = object.position.distance_to(e.position)
            if distance < shortest_distance or shortest_distance == None:
                shortest_distance = distance
                item = e
        return item

    def find_nearest_collidable(self, object, objects = None):
        item = self.find_nearest(object, objects)
        if item != None:
            if object.collide(item):
                return item
            else:
                return None
        else:
            return None
        return False
