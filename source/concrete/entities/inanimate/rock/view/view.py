from source.abstract.entities.inanimate.view import view
from source.library.action import action

from animation_config import stand

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.dimensions.x = 32
        self.dimensions.y = 32
        self.animation = action.Action(self, stand.data)
        pass

    def on_render(self):
        self.animation.on_render(self)
        pass

