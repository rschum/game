from source.abstract.entities.animate.model import model

class Model(model.Model):
    name    = "HumanEntity"
    holding = None
    reach   = 0
    
    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.radius = 50
        self.reach = self.radius
        pass
    
    def translate(self):
        model.Model.translate(self)
        if self.holding != None:
            self.holding.position.x = self.position.x
            self.holding.position.y = self.position.y
            self.holding.position.z = self.position.z

    def activate(self):
        for collidable in self.get_collisions():
            collidable.on_activate()
        pass

    def drop_item(self):
        if self.holding != None:
            self.holding.on_drop()
            self.holding = None
        pass

    def pickup(self, item = None):
        if item != None:
            self.holding = item
            self.holding.on_pickup()
            self.holding.position = self.position
            return True
        else:
            if self.holding == None:
                self.holding = self.entity_manager.find_nearest_collidable(self, self.entity_manager.entities)
                if self.holding != None:
                    self.holding.on_pickup()
                    return True
                else:
                    return False
            else:
                self.drop_item()
                return False
        return False

    def mine(self):
        tile = self.entity_manager.find_nearest_collidable(self, self.entity_manager.tiles)
        ore = tile.mine_ore()

        if ore is not None:
            homestead = self.entity_manager.find_nearest(self, self.entity_manager.homesteads)
            ore.set_parent(homestead)
            self.pickup(ore)
        pass
