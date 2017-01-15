import uuid, random
from datetime import datetime, timedelta
from source.library.science.math.geometry.g3d.sphere import sphere

class Model(sphere.Sphere):
    entity_factory  = None
    uuid            = None
    created         = None
    factory         = None
    parent          = None
    name            = "BaseObject"
    spawn_id        = 0
    spawned_number  = 0
    children        = None
    seed            = None
    collisions      = None

    def __init__(self, parent = None):
        sphere.Sphere.__init__(self)
        self.generate_seed()
        self.set_parent(parent)
        self.radius = 1
        self.children = []
        self.collisions = []
        self.uuid = uuid.uuid4()
        self.created = datetime.now()
        pass

    def spawn(self):
        self.get_collisions()
        pass

    def created_delta(self):
        return (datetime.now() - self.created).total_seconds()

    def generate_seed(self):
        if self.parent is not None:
            random.seed(self.parent.get_seed() + self.spawn_id + 1)
        else:
            random.seed(self.spawn_id + 1)
        self.seed = random.random()
        pass

    def get_seed(self):
        if self.seed is None:
            self.generate_seed()
        return self.seed

    def add_child(self, child):
        child.parent = self
        child.spawn_id = self.spawned_number
        self.children.append(child)
        self.spawned_number += 1
        pass

    def disown_child(self, child):
        self.children.remove(child)
        pass

    def set_parent(self, parent = None):
        if parent is not None:
            if self.parent is not None:
                self.parent.disown_child(self)
            parent.add_child(self)
        pass

    def get_collisions(self, object = None):
        if object is None:
            object = self
        
        universe_collisions = []
        for universe in self.entity_factory.universes:
            self.collide(self.entity_factory.universes[universe])
        """
        if object.parent is not None:
            if self.collide(object.parent):
                self.__add_collision(self.parent)
                self.__check_collisions(object.parent.get_collisions())
        self.__check_collisions(object.children)
        """
        self.collisions += universe_collisions
        return self.collisions

    def __check_collisions(self, objects):
        for object in objects:
            if object is not self:
                if self.collide(object) == True:
                    self.__add_collision(object)
                else:
                    self.__remove_collision(object)
        self.__clean_collisions()
        return self.collisions

    def __add_collision(self, object):
        if object not in self.collisions:
            self.collisions.append(object)
            self.__check_collisions(object.children)
            object.on_collide(self)
        pass

    def __add_collisions(self, objects):
        for object in objects:
            self.__check_collisions(object)
        pass

    def __remove_collision(self, object):
        if object in self.collisions:
            self.collisions.remove(object)
        pass

    def __clean_collisions(self):
        for object in self.collisions:
            if self.collide(object) == False:
                self.__remove_collision(object)
        pass

    def get_app(self):
        return self.parent.get_app()
