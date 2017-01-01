import pygame

class View:
    def __init__(self):
        pass

    def on_render(self):
        self.universe.on_render()
        self.post_render()
        pass

    def post_render(self):
        pygame.display.update()
        pygame.display.flip()
        pass
