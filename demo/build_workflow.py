#! /usr/bin/python2.7

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from source.library.science.geology.rocks import bauxite
from source.library.science.geology.rocks import ice
from source.systems.logistics import logistics
from source.concrete.entities.inanimate.rock import rock

if __name__ == "__main__":
    logistics  = logistics.Logistics()

    #Create some rocks
    ice_rock = rock.Rock(None, 1.2, ice.Ice().composition)
    bauxite_rock = rock.Rock(None, 0.95, bauxite.Bauxite().composition)

    #Print out the composition of the Minerals
    ice_rock.composition.pretty_print()
    bauxite_rock.composition.pretty_print()

    #Put Minerals in the Refinery
    print("\033[94m"+"Refining ice rock and Storing it's Elements in the Elemental Storage Unit."+"\033[0m")
    logistics.refinery.refine_mineral(ice_rock)

    print("\033[94m"+"Refining bauxite rock and Storing it's Elements in the Elemental Storage Unit."+"\033[0m")
    logistics.refinery.refine_mineral(bauxite_rock)

    #Print out the status of the ElementalStorageUnit
    logistics.elemental_storage_unit.pretty_print()

    #Replicate a Widget
    widget0 = logistics.replicator.build_widget()
    widget0.pretty_print()

    #Print out the status of the ElementalStorageUnit To see if Elements have been Removed
    logistics.elemental_storage_unit.pretty_print()

    #Replicate Another Widget
    widget1 = logistics.replicator.build_widget()
    widget1.pretty_print()

    #This Widget should fail
    widget2 = logistics.replicator.build_widget()

    #Print out the status of the ElementalStorageUnit To see if Elements have been Removed
    logistics.elemental_storage_unit.pretty_print()
