class Controller:
    def __init__(self):
        pass

    def on_loop(self):
        for uuid in self.universes:
            self.universes[uuid].on_loop()
        for uuid in self.avatars:
            self.avatars[uuid].on_loop()
