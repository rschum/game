class Model:
    number          = None
    name            = None
    symbol          = None
    mass            = None

    abundance = {
        "universe"     : 0,
        "sun"          : 0,
        "meteorite"    : 0,
        "crust"        : 0,
        "ocean"        : 0,
        "human"        : 0
    }

    def __init__(self, parent = None):
        pass
