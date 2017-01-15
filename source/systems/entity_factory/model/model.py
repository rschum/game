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
        print self.entities
        pass

    def spawn(self, entity, parent = None):
        e = entity(parent)
        e.entity_factory = self
        if(entity is avatar.Avatar):
            self.avatars[e.uuid] = e
        elif(entity is camera.Camera):
            self.camera = e
        elif(entity is galaxy.Galaxy):
            self.galaxies[e.uuid] = e
        elif(entity is hectare.Hectare):
            self.hectares[e.uuid] = e
        elif(entity is homestead.Homestead):
            self.homesteads[e.uuid] = e
        elif(entity is logistics.Logistics):
            self.logistics[e.uuid] = e
        elif(entity is kilometer.Kilometer):
            self.kilometers[e.uuid] = e
        elif(entity is planet.Planet):
            self.planets[e.uuid] = e
        elif(entity is solar_system.SolarSystem):
            self.solar_systems[e.uuid] = e
        elif(entity is tile.Tile):
            self.tiles[e.uuid] = e
        elif(entity is power_grid.PowerGrid):
            self.power_grids[e.uuid] = e
        elif(entity is universe.Universe):
            self.universes[e.uuid] = e
        else:
            self.entities[e.uuid] = e
        e.spawn()
        return e

    def get_app(self):
        return self.parent.get_app()
