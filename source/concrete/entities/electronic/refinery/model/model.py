from source.abstract.entities.inanimate.model import model

class Model(model.Model):
    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        pass

    def activate(self):
        for entity in self.parent.parent.entities:
            if entity.position.x >= self.position.x and entity.position.y >= self.position.y:
                if entity.position.x <= self.position.x + 100 and entity.position.y <= self.position.y + 100: #TODO: Magic Numbers get this from geometry
                    self.refine_mineral(entity)

    def refine_mineral(self, object):
        for component in object.composition.composition:
            portion = component[0]
            chemical = component[1]
            moles = chemical.moles_from_m3(portion * object.volume)

            for element in chemical.elements:
                self.parent.elemental_storage_unit.store_element(element, moles)
        pass
