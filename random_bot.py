import random
import numpy as np
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def randoms(game):
    move = ""
    while True:
        move = f"{random.randint(0,2)}{random.randint(0,2)}"
        if game[int(move[0])][int(move[1])] == 0:
            break 
    return move


        

    
    