import random

class Tiles():
    
    def shuffled_tiles(): 
        tiles = ['red', 'blue', 'green', 
        'purple', 'yellow', 'pink']

        random.Random(5).shuffle(tiles)
        
        return tiles