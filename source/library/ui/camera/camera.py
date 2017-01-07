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
            (int(self.resolution.x), int(self.resolution.y)),
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
        resource.blit(
            self.surface,
            (
                object.position.x + object.render_offset.x - self.position.x + (self.resolution.x / 2),
                object.position.y + object.render_offset.y - self.position.y + (self.resolution.y / 2)
            )
        )
        pass

    def render_frame(self, resource, object):
        self.draw_radius(object)
        self.surface.blit(
            resource,
            (
                object.position.x + object.render_offset.x - self.position.x + (self.resolution.x / 2),
                object.position.y + object.render_offset.y - self.position.y + (self.resolution.y / 2)
            )
        )
        pass

    def draw_radius(self, object):
        from source.abstract.entities.entity.model import model
        if isinstance(object, model.Model):
            line_width = 1
            if line_width < object.radius:
                pygame.draw.circle(
                    self.surface,
                    (0, 128, 0),
                    (
                        int(object.position.x - self.position.x + (self.resolution.x / 2)),
                        int(object.position.y - self.position.y + (self.resolution.y / 2))
                    ),
                    object.radius,
                    2
                )
        pass

    def in_viewport(self, obj):
        x = self.position.x - (self.resolution.x / 2)
        y = self.position.y - (self.resolution.y / 2)
        w = self.position.x + (self.resolution.y / 2)
        h = self.position.y + (self.resolution.y / 2)

        if obj.position.x > x or obj.position.x < w:
            if obj.position.y > y or obj.position.y < h:
                return True
        obj.animation = None
        return False
        pass
