class Controller:
    def __init__(self):
        pass

    def on_loop(self):
        self.transform()
        self.get_collisions()
        pass

    def on_activate(self):
        pass

    def on_pickup(self):
        pass

    def on_drop(self):
        self.drop()
        pass

    def on_collide(self, object = None):
        pass

    def on_1_second(self):
        print("1s")
        pass

    def on_5_second(self):
        print("5s")
        pass

    def on_10_second(self):
        print("10s")
        pass

    def on_30_second(self):
        print("30s")
        pass

    def on_1_minute(self):
        print("1m")
        pass

    def on_5_minute(self):
        print("5m")
        pass

    def on_10_minute(self):
        print("10m")
        pass

    def on_30_minute(self):
        print("30m")
        pass

    def on_1_hour(self):
        print("1h")
        pass

    def on_12_hour(self):
        print("12h")
        pass

    def on_1_day(self):
        print("1d")
        pass

    def on_1_week(self):
        print("1w")
        pass

    def on_1_month(self):
        print("1m")
        pass

    def on_1_year(self):
        print("1y")
        pass
