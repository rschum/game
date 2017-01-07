from source.abstract.entities.inanimate.model import model

class Model(model.Model):
    name    = "Refinery"

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        pass

    def activate(self):
        for entity in self.parent.parent.entities:
            if entity.position.x >= self.position.x and entity.position.y >= self.position.y:
                if entity.position.x <= self.position.x + 100 and entity.position.y <= self.position.y + 100: #TODO: Magic Numbers get this from geometry
                    self.refine_object(entity)

    def refine_object(self, entity):
        element_masses = entity.get_element_masses()
        for element_name in element_masses.keys():
            self.parent.elemental_storage_unit.store_element(element_name, element_masses[element_name])
        self.parent.parent.remove_entity(entity)
        pass
