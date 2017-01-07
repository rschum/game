from source.abstract.entities.inanimate.model import model

class Model(model.Model):
    name    = "Replicator"
    
    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        pass

    def activate(self):
        self.build_widget()

    def build_widget(self):
        from source.concrete.entities.inanimate.rock import rock
        from source.library.science.geology.rocks import bauxite

        widget = rock.Rock(self.parent, 0.95, bauxite.Bauxite().composition)
        
        if self.parent.elemental_storage_unit.check_storage(widget.composition.composition):
            print("\033[94m"+"Building Widget"+"\033[0m")
            self.parent.elemental_storage_unit.take_elements(widget.composition.composition)
            widget.position.x = self.position.x
            widget.position.y = self.position.y
            if self.parent.parent != None:
                self.parent.parent.entities.append(widget)
            return widget
        else:
            print("\033[91m"+"Build Failed."+"\033[0m")
            return None
        pass
