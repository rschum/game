class Composition:

    def __init__(self, list=None):
        # normalizes input to an array of complimentary proportions
        total = sum(i[0] for i in list)
        self.composition = [(part[0] / total, part[1]) for part in list]
        pass


    def pretty_print(self, i=0):
        for member in self.composition:
            print ("\t" * i), member[0], "\t", member[1].name

