from source.abstract.base_object.view import view

import pygame

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        pass

    def render(self):
        view.View.render(self)
        self.entity_factory.on_render()
        pass

    def post_render(self):
        pygame.display.update()
        pygame.display.flip()
        pass
