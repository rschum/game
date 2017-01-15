import pygame
from source.global_variables import global_variables

from source.abstract.entities.entity.model import model

class Model(model.Model):
    surface    = None
    flags      = None
    depth      = 32

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.radius = self.dimensions.x / 2
        self.flags = pygame.HWSURFACE | pygame.DOUBLEBUF
        pass

    def spawn(self):
        model.Model.spawn(self)
        self.surface = pygame.display.set_mode(
            (
                int(self.dimensions.x),
                int(self.dimensions.y)
            ),
            self.flags,
            self.depth
        )
        pass

    def set_target(self, target):
        self.position = target.position
        pass

    def fill_surface(self):
        self.surface.fill(global_variables.BGCOLOR)
        pass

    def pre_render(self):
        self.fill_surface()
        pass

    def render_animation(self, resource, object):
        self.draw_radius(object)
        pos = self.render_offset_position(object)
        resource.blit(
            self.surface,
            (
                pos.x,
                pos.y
            )
        )
        pass

    def render_frame(self, resource, object):
        self.draw_radius(object)
        pos = self.render_offset_position(object)
        self.surface.blit(
            resource,
            (
                pos.x,
                pos.y
            )
        )
        pass

    def draw_radius(self, object):
        if object.draw_radius == True:
            from source.abstract.entities.entity.model import model
            if isinstance(object, model.Model):
                if object.stroke < object.radius:
                    pos = self.render_position(object)
                    pygame.draw.circle(
                        self.surface,
                        object.stroke_color,
                        (
                            int(pos.x),
                            int(pos.y)
                        ),
                        object.radius,
                        object.stroke
                    )
        pass

    def render_position(self, object):
        return object.position - self.position + (self.dimensions / 2)

    def render_offset_position(self, object):
        return self.render_position(object) + object.get_render_offset()

    def in_viewport(self, object):
        pos_0 = self.position - (self.dimensions / 2)
        pos_1 = self.position + (self.dimensions / 2)
        
        if object.position.x > pos_0.x or object.position.x < pos_1.x:
            if object.position.y > pos_0.y or object.position.y < pos_1.y:
                return True
        object.animation = None
        return False
