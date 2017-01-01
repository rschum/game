class Controller:
    def __init__(self):
        pass

    def on_loop(self):
        self.charge()

        for drain in self.drains:
            drain.discharge()
        pass
