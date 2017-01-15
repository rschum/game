class View:
    def __init__(self):
        pass

    def on_render(self):
        self.camera.pre_render()
        for uuid in self.universes:
            self.universes[uuid].on_render()
        for uuid in self.avatars:
            self.avatars[uuid].on_render()
