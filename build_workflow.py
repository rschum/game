#! /usr/bin/python2.7

from source.chemistry.rocks import bauxite
from source.chemistry.rocks import ice
from source.systems.logistics import logistics

if __name__ == "__main__":
    logistics  = logistics.Logistics()

    #Create some rocks
    ice = ice.Ice()
    bauxite = bauxite.Bauxite()

    #Print out the composition of the Minerals
    ice.pretty_print()
    bauxite.pretty_print()

    #Put Minerals in the Refinery
    logistics.refinery.refine_mineral(ice)
    logistics.refinery.refine_mineral(bauxite)

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
