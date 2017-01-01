class Controller:
    def __init__(self):
        pass

    def on_loop(self):
        self.transform()
        pass

    def on_pickup(self, parent):
        parent.transform()
        pass

    def on_drop(self):
        pass
