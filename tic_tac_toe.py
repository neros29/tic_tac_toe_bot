from random_bot import *

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def print_game():
    for i in game:
        z = ""
        for x in i:
            if x == 0:
                z += "_"
            elif x == 1:
                z += "X"
            elif x == -1:
                z += "O"
        print(z)
        
        
def commpleted():
    for i in game:
        if sum(i)**2 == 3**2:
            return True
    for i in range(3):
        if (game[0][i] + game[1][i] + game[2][i])**2 == 3**2:
            return True
    if (game[0][0] + game[1][1] + game[2][2])**2 == 3**2:
        return True
    if (game[0][2] + game[1][1] + game[2][0])**2 == 3**2:
        return True
    return False
        

run = True
while run:
    try:
        p1 = input("p1's moves")
        if game[int(p1[0])][int(p1[1])] == 0:
            game[int(p1[0])][int(p1[1])] = 1
        else:
            print("not a valid move")
            continue
    except:
        print("invalid move")
        continue
    if commpleted() == True:
        print("winner winner chicken dinner")
        break
    print_game()
    while True:
        try:
            p2 = randoms(game)
            if game[int(p2[0])][int(p2[1])] == 0:
                game[int(p2[0])][int(p2[1])] = -1
                break
            else:
                print("not a valid move")
        except:
            print("invalid move")
            continue 

        
    
    if commpleted() == True:
        print("winner winner chican dinner")
        break
    print_game()
print_game()

                        