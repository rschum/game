from source.abstract.entities.electronic.model import model

class Model(model.Model):
    name        = "Replicator"
    logistics   = None
    
    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.radius = 50
        self.mass = 30
        pass

    def activate(self):
        self.build_widget()

    def build_widget(self):
        from source.concrete.entities.inanimate.rock import rock
        from source.library.science.geology.rocks import bauxite

        widget = self.entity_manager.spawn(rock.Rock, self.parent)
        widget.mass = 100
        widget.set_material(bauxite.Bauxite())
        widget.position.x = self.position.x
        widget.position.y = self.position.y
        # TODO: widget = solarPanel

        element_requirements = widget.get_element_masses()
        if self.logistics.check_storage(element_requirements):
            print("\033[94m"+"Building Widget"+"\033[0m")
            self.logistics.take_elements(element_requirements)
            return widget
        else:
            print("\033[91m"+"Build Failed."+"\033[0m")
            return None
        return False
