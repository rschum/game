class Composition:

    def __init__(self):
        pass

    def normalize(self, raw_composition):
        # normalizes input to an array of complimentary proportions
        total = sum(i[0] for i in raw_composition)
        norm_composition = [(part[0] / total, part[1]) for part in raw_composition]
        return norm_composition

    @staticmethod
    def pretty_print(composition, i=0):
        for member in composition:
            print ("\t" * i), member[0], "\t", member[1].name

