import pygame
from source.global_variables import global_variables

class Camera:
    surface    = None
    position   = None
    center     = None
    resolution = None
    flags      = pygame.HWSURFACE
    depth      = 32

    def __init__(self):
        self.position   = pygame.math.Vector3(0, 0, 0)
        self.resolution = pygame.math.Vector3(global_variables.RESOLUTION_X, global_variables.RESOLUTION_Y, 0)
        self.center     = pygame.math.Vector3(self.resolution.x / 2, self.resolution.y / 2, 0)

        self.surface = pygame.display.set_mode(
            (
                int(self.resolution.x),
                int(self.resolution.y)
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

    def render_animation(self, resource, object):
        self.draw_radius(object)
        pos = object.position + object.get_render_offset() - self.position + (self.resolution / 2)
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
        pos = object.position + object.get_render_offset() - self.position + (self.resolution / 2)
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
                line_width = 1
                if line_width < object.radius:
                    pos = object.position - self.position + (self.resolution / 2)
                    pygame.draw.circle(
                        self.surface,
                        (0, 128, 0),
                        (
                            int(pos.x),
                            int(pos.y)
                        ),
                        object.radius,
                        2
                    )
        pass

    def in_viewport(self, object):
        pos_0 = self.position - (self.resolution / 2)
        pos_1 = self.position + (self.resolution / 2)
        
        if object.position.x > pos_0.x or object.position.x < pos_1.x:
            if object.position.y > pos_0.y or object.position.y < pos_1.y:
                return True
        object.animation = None
        return False
