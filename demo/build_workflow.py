#! /usr/bin/python2.7

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from source.library.science.geology.rocks import bauxite
from source.library.science.geology.rocks import ice
from source.concrete.entities.inanimate.rock import rock
from source.abstract.location.model import model
from source.systems.logistics import logistics
from source.concrete.entities.electronic.elemental_storage_unit import elemental_storage_unit
from source.concrete.entities.electronic.elemental_storage_tank import elemental_storage_tank
from source.concrete.entities.electronic.refinery import refinery
from source.concrete.entities.electronic.replicator import replicator

class BuildWorkflow(model.Model):
    entities    = []
    logistics   = None

    def __init__(self):
        model.Model.__init__(self)

        self.add_logistics()
        self.add_rocks()

    def add_rocks(self):
        ice_rock = rock.Rock(self, 100, ice.Ice())
        bauxite_rock = rock.Rock(self, 100, bauxite.Bauxite())
        
        self.add_entity(ice_rock)
        self.add_entity(bauxite_rock)
        pass

    def add_logistics(self):
        self.logistics = logistics.Logistics(self)

        elemental_storage_unit0 = elemental_storage_unit.ElementalStorageUnit(self, self.logistics)
        self.add_entity(elemental_storage_unit0)
        
        refinery0 = refinery.Refinery(self, self.logistics)
        self.add_entity(refinery0)
        
        replicator0 = replicator.Replicator(self, self.logistics)
        self.add_entity(replicator0)
        pass

    def print_composition_of_minerals(self):
        for entity in self.entities:
            if isinstance(entity, rock.Rock):
                entity.material.pretty_print()

    def put_minerals_in_the_refinery(self):
        for entity in self.entities:
            if isinstance(entity, rock.Rock):
                print("\033[94m"+"Refining rock and Storing it's Elements in the Elemental Storage Unit."+"\033[0m")
                self.logistics.refinery.refine_object(entity)

    def print_the_status_of_the_elemental_storage_unit(self):
        self.logistics.elemental_storage_unit.pretty_print()

    def replicate_a_widget(self):
        widget0 = self.logistics.replicator.build_widget()
        if widget0 != None:
            widget0.pretty_print()

    def print_entities(self):
        for entity in self.entities:
            entity.pretty_print()

if __name__ == "__main__":
    build_workflow = BuildWorkflow()
    build_workflow.print_composition_of_minerals()
    build_workflow.put_minerals_in_the_refinery()
    build_workflow.print_the_status_of_the_elemental_storage_unit()
    build_workflow.replicate_a_widget()
    build_workflow.replicate_a_widget()
    build_workflow.print_the_status_of_the_elemental_storage_unit()
    build_workflow.print_entities()
