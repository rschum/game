class Rock:
    name = None
    composition = None
    
    def __init__(self):
        pass

    def pretty_print(self, i=0):
        print(("\t"*i) + self.name)
        self.composition.pretty_print(i+1)
