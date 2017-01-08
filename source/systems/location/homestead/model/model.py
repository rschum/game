from source.abstract.location.model import model

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

class Model(model.Model):
    power_grid      = None
    logistics       = None
    battery0        = None

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)

        rock0 = rock.Rock(self, 100, ice.Ice())
        rock0.position.x = 50
        rock0.position.y = 250
        self.add_entity(rock0)

        corn0 = corn.Corn(self)
        corn0.position.x = 150
        corn0.position.y = 250
        self.add_entity(corn0)

        turnip0 = turnip.Turnip(self)
        turnip0.position.x = 350
        turnip0.position.y = 250
        self.add_entity(turnip0)
        
        tomato0 = tomato.Tomato(self)
        tomato0.position.x = 250
        tomato0.position.y = 250
        self.add_entity(tomato0)

        potato0 = potato.Potato(self)
        potato0.position.x = 450
        potato0.position.y = 250
        self.add_entity(potato0)

        self.power_grid = power_grid.PowerGrid()

        solar_panel_0 = solar_panel.SolarPanel(self)
        solar_panel_0.position.x = 50
        solar_panel_0.position.y = 50
        self.power_grid.attach_source(solar_panel_0)
        self.add_entity(solar_panel_0)

        solar_panel_1 = solar_panel.SolarPanel(self)
        solar_panel_1.position.x = 50
        solar_panel_1.position.y = 150
        self.power_grid.attach_source(solar_panel_1)
        self.add_entity(solar_panel_1)

        self.battery0 = battery.Battery(self)
        self.battery0.position.x = 150
        self.battery0.position.y = 50
        self.battery0.charge = 21
        self.power_grid.attach_store(self.battery0)
        self.add_entity(self.battery0)

        lightbulb0 = lightbulb.LightBulb(self)
        lightbulb0.position.x = 250
        lightbulb0.position.y = 50
        self.power_grid.attach_drain(lightbulb0)
        self.add_entity(lightbulb0)

        #self.npc = npc.NPC(self)
        #self.npc.position.x = 50
        #self.npc.position.y = 250
        #self.add_entity(self.npc)

        self.logistics = logistics.Logistics(self)
        self.logistics.refinery.position.x = 50
        self.logistics.refinery.position.y = 350
        self.logistics.elemental_storage_unit.position.x = 150
        self.logistics.elemental_storage_unit.position.y = 350
        self.logistics.replicator.position.x = 250
        self.logistics.replicator.position.y = 350

        x = 50
        for tank in self.logistics.elemental_storage_unit.tanks:
            self.logistics.elemental_storage_unit.tanks[tank].position.x = x
            self.logistics.elemental_storage_unit.tanks[tank].position.y = 450
            x += 50
        pass
