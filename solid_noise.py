#! /usr/bin/python2.7

from source.library.solid_noise import union_map#solid_noise, planet

if __name__ == "__main__":
    map = union_map.UnionMap(None)
    map.complexity  = 10 #Low values make smooth terrain. High values make detailed terrain
    map.x_axis      = 157 #Map Scale
    map.y_axis      = 100 #Map Scale
    #map.x_offset    = -0.5 #Scroll around an infinate map
    #map.y_offset    = -0.5 #Scroll around an infinate map
    map.load() #this loads above values so they can generate a map
    map.generate_noise_map() #Generate an entire map based on above inputs and store it in an array

    print map.noise_map.min() #lowest point on map
    print map.noise_map.max() #highest point on map

    print map.noise_map[50][50] #Get a value from the map array

    print map.get_noise(50, 50) #This should be slightly different because it's pulling directly from the raw data

    map.show() #display map in a matplotlib window
