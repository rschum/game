from source.abstract.location.controller import controller
from source.library.ui import keyboard
from source.library.solid_noise import union_map

class Controller(controller.Controller):
    def __init__(self):
        controller.Controller.__init__(self)
        keyboard.KEY_P.subscribe(self)
        pass

    def on_loop(self):
        for kilometer in self.kilometers:
            for kilo in kilometer:
                kilo.on_loop()
        controller.Controller.on_loop(self)
        pass

    def on_keydown_p(self):
        map = union_map.UnionMap(None)
        map.complexity  = 10 #Low values make smooth terrain. High values make detailed terrain
        map.x_axis      = 157 #Map Scale
        map.y_axis      = 100 #Map Scale
        #map.x_offset    = -0.5 #Scroll around an infinate map
        #map.y_offset    = -0.5 #Scroll around an infinate map
        map.load() #this loads above values so they can generate a map
        map.generate_noise_map()
        map.show()
        pass

    def on_keyup_p(self):
        pass
