from pygame import math
from source.library.action import action
from animation_config import stand

class View:
    height = None
    width  = None

    animation = None

    render_offset = None

    draw_radius = True
    
    height  = 0
    width   = 0

    def __init__(self):
        self.render_offset = math.Vector3(0, 0, 0)
        pass

    def get_render_offset(self):
        self.render_offset.x = -(self.width / 2)
        self.render_offset.y = -(self.height)
        return self.render_offset

    def set_animation(self):
        if abs(self.speed().length()) == 0:
            if self.animation == None or self.animation.action != "stand":
                self.animation = action.Action(stand.data)

    def on_render(self):
        self.set_animation()
        self.animation.on_render(self)
        pass

    def pretty_print(self, i = 0):
        print(" "*i)
