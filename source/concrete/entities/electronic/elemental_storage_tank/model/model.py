from source.abstract.entities.inanimate.model import model

class CapacityState:
    PERCENT_000 = 0
    PERCENT_020 = 1
    PERCENT_040 = 2
    PERCENT_060 = 3
    PERCENT_080 = 4
    PERCENT_100 = 5

class Model(model.Model):
    element         = None
    stored          = 0 # in moles
    capacity        = None # in moles
    capacity_state  = CapacityState.PERCENT_000

    def __init__(self, parent, element, capacity = 100000):
        model.Model.__init__(self, parent)
        self.element = element
        self.capacity = capacity
        pass

    def add_element(self, moles):
        # spherical_cow: storage should be of chemicals rather than elements.
        # spherical_cow: storage should be in cubic meters, using the density of the stored chemical.
        if self.stored == self.capacity:
            print("\033[91m"+self.element+" Storage Tank is Full. "+self.element+" Has Been Wasted.\033[0m")
        elif self.capacity - self.stored < moles:
            print("\033[91m Only some " + self.element + " was stored. " + self.element + " Has Been Wasted.\033[0m")
            self.stored = self.capacity
        else:
            print("\033[92m"+self.element+" Stored.\033[0m")
            self.stored += moles
        pass

    def remove_elements(self, amount):
        self.stored -= amount

    def get_stored_percent(self):
        return float(self.stored) / float(self.capacity)
