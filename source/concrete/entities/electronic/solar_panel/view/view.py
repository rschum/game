from source.abstract.entities.inanimate.view import view
from source.library.action import action

from animation_config import stand

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.animation = action.Action(stand.stand_data)
        self.height = 32
        self.width = 32
        pass

    def on_render(self):
        self.animation.on_render(self)
        pass
