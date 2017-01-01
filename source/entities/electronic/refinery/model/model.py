from source.abstract.entities.inanimate.model import model

class Model(model.Model):
    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        pass

    def refine_mineral(self, object):
        # spherical_cow: for simplicity we'll assume the composition is in terms of volume
        for component in object.composition.composition:
            portion = component[0]
            chemical = component[1]
            moles = chemical.moles_from_m3(portion * object.volume)

            for element in chemical.elements:
                self.parent.elemental_storage_unit.store_element(element, moles)
        pass
