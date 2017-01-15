class Controller:
    is_loopable     = True
    is_collidable   = True

    def __init__(self):
        pass

    def on_loop(self):
        if self.is_loopable:
            for child in self.children:
                child.on_loop()
            self.transform()
        pass

    def on_activate(self):
        pass

    def on_move(self):
        self.get_collisions()

    def on_collide(self, entity = None):
        if self.is_collidable:
            pass
        pass

