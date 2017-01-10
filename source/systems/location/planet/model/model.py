from source.abstract.location.model import model
from source.global_variables import camera
from source.systems.location.kilometer import kilometer
from source.systems.location.homestead import homestead
from source.concrete.entities.human.avatar import avatar

class Model(model.Model):
    avatar          = None
    camera          = None
    homestead       = None

    size            = 1
    kilometers      = [[]]

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.populate_kilometers()

        self.homestead = homestead.Homestead(self)

        self.avatar = avatar.Avatar(self)
        #self.avatar.position.x = 300
        #self.avatar.position.y = 300

        self.camera = camera.CAMERA
        self.camera.set_target(self.avatar)
        pass

    def populate_kilometers(self):
        self.kilometers = [[kilometer.Kilometer(self) for x in range(self.size)] for y in range(self.size)]
        pass

    def get_planet(self):
        return self

    def get_kilometer(self):
        pass

    def get_hectare(self):
        pass

    def get_tile(self):
        pass
