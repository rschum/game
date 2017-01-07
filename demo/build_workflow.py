#! /usr/bin/python2.7

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from source.library.science.geology.rocks import bauxite
from source.library.science.geology.rocks import ice
from source.systems.logistics import logistics
from source.concrete.entities.inanimate.rock import rock
from source.abstract.location.model import model


class BuildWorkflow(model.Model):
    entities    = []
    logistics   = None

    def __init__(self):
        model.Model.__init__(self)
        self.logistics  = logistics.Logistics(self)

        #Create some rocks
        ice_rock = rock.Rock(self, 100, ice.Ice())
        bauxite_rock = rock.Rock(self, 100, bauxite.Bauxite())
        
        self.add_entity(ice_rock)
        self.add_entity(bauxite_rock)

    def print_composition_of_minerals(self):
        for entity in self.entities:
            entity.material.pretty_print()

    def put_minerals_in_the_refinery(self):
        while len(self.entities):
            entity = self.entities[0]
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
