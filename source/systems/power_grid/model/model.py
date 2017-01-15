from source.abstract.location.model import model

class Model(model.Model):
    sources = []
    stores  = []
    drains   = []

    grid = None

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        pass

    def attach_source(self, object):
        object.grid = self
        self.sources.append(object)
        pass

    def attach_store(self, object):
        object.grid = self
        self.stores.append(object)
        pass

    def attach_drain(self, object):
        object.grid = self
        self.drains.append(object)
        pass

    def get_charge(self):
        charge = 0
        for store in self.stores:
            charge += store.charge
        return charge

    def charge(self):
        charge = 0
        for source in self.sources:
            source.delta_charge()
            charge += source.charge
            source.charge = 0

        for store in self.stores:
            #TODO: This will charge all stores with the charge amount. Instead, it should divide amongst the stores / charge
            #TODO: Check if adding a charge will go over 100%, if so, add to a different source
            #TODO: Overcharging damages store?
            store.charge += charge
        pass

    def discharge(self, i):
        charge = 0
        for store in self.stores:
            if store.charge >= i:
                store.charge -= i
                charge += i
            else:
                charge += store.charge
                store.charge = 0
        return charge
