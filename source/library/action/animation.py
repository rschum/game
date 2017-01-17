import pygame
from libs.pyganim import pyganim

class Animation:
    parent              = None
    entity_name         = None
    path_to_images      = "resources/images/"
    action              = None
    direction           = None
    animation_object    = None
    directory           = None
    move_conductor      = None

    def __init__(self, parent, data, animation):
        self.parent         = parent
        self.entity_name    = data["entity_name"]
        self.action         = data["action"]
        self.direction      = animation["direction"]
        self.load_frames(animation["frames"])
        pass
    
    def path_to_animations(self):
        return self.path_to_images+self.entity_name+"/animations/"

    def load_frames(self, frames):
        if len(frames) > 1:
            self.load_animation(frames)
        else:
            self.load_frame(frames)
        pass

    def load_animation(self, frame):
        frames = []
        for fr in frame:
            tmp_frame = self.path_to_animations()+self.action+'/'+self.direction+'/'+fr[0]
            tmp_duration = fr[1]
            fra = (tmp_frame, tmp_duration)
            frames.append(fra)
            self.animation_object = pyganim.PygAnimation(frames)
            self.move_conductor = pyganim.PygConductor(self.animation_object)

    def load_frame(self, frame):
        tmp_frame = self.path_to_animations()+self.action+'/'+self.direction+'/'+frame[0][0]
        f = pygame.image.load(tmp_frame).convert_alpha()
        self.animation_object = f

    def on_render(self, object):
        if isinstance(self.animation_object, pyganim.PygAnimation):
            self.move_conductor.play()
            self.parent.get_app().entity_manager.camera.render_animation(self.animation_object, object)
        else:
            self.parent.get_app().entity_manager.camera.render_frame(self.animation_object, object)
        pass
