class Controller:
    def __init__(self):
        pass

    def on_loop(self):
        self.transform()
        self.get_collisions()
        pass

    def on_pickup(self):
        pass

    def on_drop(self):
        self.drop()
        pass

    def on_collide(self, object = None):
        pass
