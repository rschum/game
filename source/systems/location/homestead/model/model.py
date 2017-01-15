from source.abstract.location.model import model

from pygame import math

from source.library.science.geology.rocks import ice
from source.systems.power_grid import power_grid
from source.concrete.entities.plant.corn import corn
from source.concrete.entities.plant.turnip import turnip
from source.concrete.entities.plant.tomato import tomato
from source.concrete.entities.plant.potato import potato
from source.concrete.entities.electronic.solar_panel import solar_panel
from source.concrete.entities.electronic.battery import battery
from source.concrete.entities.electronic.lightbulb import lightbulb
from source.concrete.entities.inanimate.rock import rock
from source.systems.logistics import logistics
from source.concrete.entities.electronic.elemental_storage_tank import elemental_storage_tank
from source.concrete.entities.electronic.refinery import refinery
from source.concrete.entities.electronic.replicator import replicator
from source.library.science.chemistry.element import elements

class Model(model.Model):
    power_grid  = None
    logistics   = None

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.name = "Homestead"
        self.dimensions = math.Vector3(10000, 10000, 10000)
        self.radius = self.dimensions.x / 2
        pass

    def spawn(self):
        model.Model.spawn(self)
        self.add_logistics()
        self.add_power_grid()
        self.add_crops()
        pass

    def add_crops(self):
        corn0 = self.entity_factory.spawn(corn.Corn, self)
        corn0.position.x = 50
        corn0.position.y = 250

        turnip0 = self.entity_factory.spawn(turnip.Turnip, self)
        turnip0.position.x = 150
        turnip0.position.y = 250
        
        tomato0 = self.entity_factory.spawn(tomato.Tomato, self)
        tomato0.position.x = 250
        tomato0.position.y = 250

        potato0 = self.entity_factory.spawn(potato.Potato, self)
        potato0.position.x = 350
        potato0.position.y = 250
        pass

    def add_logistics(self):
        self.logistics = self.entity_factory.spawn(logistics.Logistics, self)

        refinery0 = self.entity_factory.spawn(refinery.Refinery, self)
        refinery0.position.x = 50
        refinery0.position.y = 350
        self.logistics.add_refinery(refinery0)
        
        replicator0 = self.entity_factory.spawn(replicator.Replicator, self)
        replicator0.position.x = 250
        replicator0.position.y = 350
        self.logistics.add_replicator(self)

        aluminum_tank = self.entity_factory.spawn(elemental_storage_tank.ElementalStorageTank, self)
        aluminum_tank.element = elements.Aluminum
        aluminum_tank.capacity = 100
        aluminum_tank.position.x = 50
        aluminum_tank.position.y = 450
        self.logistics.add_tank(aluminum_tank)
        
        carbon_tank = self.entity_factory.spawn(elemental_storage_tank.ElementalStorageTank, self)
        carbon_tank.element = elements.Carbon
        carbon_tank.capacity = 100
        carbon_tank.position.x = 100
        carbon_tank.position.y = 450
        self.logistics.add_tank(carbon_tank)
        
        hydrogen_tank = self.entity_factory.spawn(elemental_storage_tank.ElementalStorageTank, self)
        hydrogen_tank.element = elements.Hydrogen
        hydrogen_tank.capacity = 100
        hydrogen_tank.position.x = 150
        hydrogen_tank.position.y = 450
        self.logistics.add_tank(hydrogen_tank)

        iron_tank = self.entity_factory.spawn(elemental_storage_tank.ElementalStorageTank, self)
        iron_tank.element = elements.Iron
        iron_tank.capacity = 100
        iron_tank.position.x = 200
        iron_tank.position.y = 450
        self.logistics.add_tank(iron_tank)

        oxygen_tank = self.entity_factory.spawn(elemental_storage_tank.ElementalStorageTank, self)
        oxygen_tank.element = elements.Oxygen
        oxygen_tank.capacity = 100
        oxygen_tank.position.x = 250
        oxygen_tank.position.y = 450
        self.logistics.add_tank(oxygen_tank)

        silicon_tank = self.entity_factory.spawn(elemental_storage_tank.ElementalStorageTank, self)
        silicon_tank.element = elements.Silicon
        silicon_tank.capacity = 100
        silicon_tank.position.x = 300
        silicon_tank.position.y = 450
        self.logistics.add_tank(silicon_tank)

        calcium_tank = self.entity_factory.spawn(elemental_storage_tank.ElementalStorageTank, self)
        calcium_tank.element = elements.Calcium
        calcium_tank.capacity = 100
        calcium_tank.position.x = 350
        calcium_tank.position.y = 450
        self.logistics.add_tank(calcium_tank)

        titanium_tank = self.entity_factory.spawn(elemental_storage_tank.ElementalStorageTank, self)
        titanium_tank.element = elements.Titanium
        titanium_tank.capacity = 100
        titanium_tank.position.x = 400
        titanium_tank.position.y = 450
        self.logistics.add_tank(titanium_tank)
    
    def add_power_grid(self):
        self.power_grid = self.entity_factory.spawn(power_grid.PowerGrid, self)

        solar_panel_0 = self.entity_factory.spawn(solar_panel.SolarPanel, self)
        solar_panel_0.position.x = 50
        solar_panel_0.position.y = 50
        self.power_grid.attach_source(solar_panel_0)

        solar_panel_1 = self.entity_factory.spawn(solar_panel.SolarPanel, self)
        solar_panel_1.position.x = 50
        solar_panel_1.position.y = 150
        self.power_grid.attach_source(solar_panel_1)

        battery0 = self.entity_factory.spawn(battery.Battery, self)
        battery0.position.x = 150
        battery0.position.y = 50
        battery0.charge = 21
        self.power_grid.attach_store(battery0)

        lightbulb0 = self.entity_factory.spawn(lightbulb.LightBulb, self)
        lightbulb0.position.x = 250
        lightbulb0.position.y = 50
        self.power_grid.attach_drain(lightbulb0)
        pass

    def get_planet(self):
        return self.parent.get_planet()
