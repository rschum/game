from source.abstract.location.model import model

from source.concrete.entities.electronic.elemental_storage_unit import elemental_storage_unit
from source.concrete.entities.electronic.refinery import refinery
from source.concrete.entities.electronic.replicator import replicator

class Model(model.Model):
    name = "Logistics"
    elemental_storage_unit  = None
    refinery                = None
    replicator              = None

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.elemental_storage_unit  = elemental_storage_unit.ElementalStorageUnit(self)
        self.refinery                = refinery.Refinery(self)
        self.replicator              = replicator.Replicator(self)
        pass
