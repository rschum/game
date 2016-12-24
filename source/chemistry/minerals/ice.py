from source.chemistry import mineral
from source.chemistry import water


class Ice(mineral.Mineral):
    name = "Ice"

    def __init__(self):
        mineral.Mineral.__init__(self)
        self.chemicals = [
            water.Water()
        ]
