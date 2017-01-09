from animation_config import stand
from source.abstract.entities.electronic.view import view
from source.library.action import action


class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.dimensions.x = 100
        self.dimensions.y = 100
        self.animation = action.Action(stand.data)
        pass

    def get_render_offset(self):
        self.render_offset = -(self.dimensions / 2)
        return self.render_offset
    
    def pretty_print(self, i=0):
        print(("\t"*i)+self.name)
        
        for tank in self.tanks:
            self.tanks[tank].pretty_print(i+1)
        pass

    def on_render(self):
        view.View.on_render(self)
        for tank in self.tanks:
            self.tanks[tank].on_render()
        pass
