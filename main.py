import random
import time
turn = 0
hitstack = []



def check_already_hit(col, row, grid):
    return grid[col][row] == "X" or grid[col][row] == "M"
        

def make_ocean_grid():
    g = []
    for i in range(10):
        row = []
        for j in range(10): 
            row.append("0")
        g.append(row)
    return g

def make_target_grid():
    g = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append("O")
        g.append(row)
    return g
        
def print_ocean_grid(grid):
    print("OCEAN - GRID")
    print("  1 2 3 4 5 6 7 8 9 10")
    for i in range(10):
        for j in range(10):
            if j == 0:
                row = i + 1
                if row == 1:
                    row = "A"
                elif row == 2:
                    row = "B"
                elif row == 3:
                    row = "C"
                elif row == 4:
                    row = "D"
                elif row == 5:
                    row = "E"
                elif row == 6:
                    row = "F"
                elif row == 7:
                    row = "G"
                elif row == 8:
                    row = "H"
                elif row == 9:
                    row = "I"
                elif row == 10:
                    row = "J"

                print(row, end=" ")

            print(grid[i][j], end=" ")
        print()

def print_target_grid(grid):
    print("TARGETS - GRID")
    print("  1 2 3 4 5 6 7 8 9 10")
    for i in range(10):
        for j in range(10):
            if j == 0:
                col = i
                if col == 0:
                    col = "A"
                elif col == 1:
                    col = "B"
                elif col == 2:
                    col = "C"
                elif col == 3:
                    col = "D"
                elif col == 4:
                    col = "E"
                elif col == 5:
                    col = "F"
                elif col == 6:
                    col = "G"
                elif col == 7:
                    col = "H"
                elif col == 8:
                    col = "I"
                elif col == 9:
                    col = "J"

                print(col, end=" ")

            print(grid[i][j], end=" ")
        print()

class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.hp = size
        self.positions = [] 

def make_ships():
    ships = []
    ships.append(Ship("CARRIER", 5))
    ships.append(Ship("SUBMARINE", 1))
    ships.append(Ship("BATTLESHIP", 4))
    ships.append(Ship("CORSAIR", 2))
    ships.append(Ship("CRUISER", 3))
    return ships

def place_ship(grid, ship):
    while True:

        dir = random.randint(0, 1)
        randX = 0
        randY = 0

        if dir == 0:
            randX = random.randint(0, 10 - ship.size)
            randY = random.randint(0, 9)
        elif  dir == 1:
            randY = random.randint(0, 10 - ship.size)
            randX = random.randint(0, 9)

        isEmpty = True
        if dir == 0:
            for i in range(ship.size):
                if grid[randY][randX + i] != "0":
                    isEmpty = False
        elif  dir == 1:
            for i in range(ship.size):
                if grid[randY + i][randX] != "0":
                    isEmpty = False
        
        if isEmpty:
            if dir == 0:
                for i in range(ship.size):
                    grid[randY][randX + i] = str(ship.size)
                    ship.positions.append([randX + i, randY]) 
                
            elif  dir == 1:
                for i in range(ship.size):
                    grid[randY + i][randX] = str(ship.size)
                    ship.positions.append([randX, randY + i])
            break
        
def call_shot(coords, enemyShips, enemyGrid, targetGrid, isPlayer):
    global winCondition, turn
    col = coords[0]
    row = coords[1:]             
    col = ord(col) - 65

    row = int(row) - 1

    # for i in range(10):
    #     print()

    if targetGrid[col][row] != "X" and targetGrid[col][row] != "0":
        hit = False
        hitShip = ""
        enemyGrid[col][row] = "M"

        for ship in enemyShips:

            for position in ship.positions:
                if position[0] == row and position[1] == col:
                    hit = True
                    hitShip = ship.name
                    ship.hp -= 1
                    ship.size -= 1
                    if ship.hp == 0:
                        enemyShips.remove(ship)
                    targetGrid[col][row] = "X"
                    
                    for pos in ship.positions:
                        if pos[1] == col and pos[0] == row:
                            enemyGrid[pos[1]][pos[0]] = "X"
                        else:
                            enemyGrid[pos[1]][pos[0]] = str(ship.hp)
                        

                    ship.positions.remove(position)
                    
    
        if hit == True:
            if isPlayer == True:
                # print("HIT THE ENEMY'S " + hitShip + "!")
                ...
            elif isPlayer == False:
                # print("THE ENEMY TOOK DOWN YOUR " + hitShip + " AT " + str(coords) + "!")
                ...
            
        elif hit == False:
            if isPlayer == True:
                # print("MISS!")
                ...
            elif isPlayer == False:
                # print("THE ENEMY MISSED AT " + str(coords) + "!")
                ...
            targetGrid[col][row] = "0"

        turn += 1
        if turn > 1:
            turn = 0

    elif targetGrid[col][row] == "X" or targetGrid[col][row] == "0":
        if isPlayer == True:
            # print("INVALID TARGET.")  
            ...


def hunt(enemyGrid):
    global hitstack
    col = 0
    row = 0
    if len(hitstack) == 0:
        while True:
            col = random.randint(0, 9)
            row = random.randint(0, 9)

            if enemyGrid[col][row] != "X" and enemyGrid[col][row] != "M":
                break

    elif len(hitstack) > 0:
        col = hitstack[-1][0]
        row = hitstack[-1][1] 

    if enemyGrid[col][row] == "0":
       col = chr(col + 65)
       return str(col) + str(row + 1)
    # print("before: ", hitstack)

    if len(hitstack) > 0:
        hitstack.pop()
        print(col, row)
    # print("after: ", hitstack)

    top, down, left, right = -1, -1, -1, -1
    if col - 1 >= 0:
        top = col - 1
    if col + 1 <= 9:
        down = col + 1
    if row - 1 >= 0:
        left = row - 1
    if row + 1 <= 9:
        right = row + 1
        
    if top != -1 and not check_already_hit(top, row, enemyGrid):
        hitstack.append([top, row])
        
    if down != -1 and not check_already_hit(down, row, enemyGrid):
        hitstack.append([down, row])
        
    if left != -1 and not check_already_hit(col, left, enemyGrid):
        hitstack.append([col, left])
        
    if right != -1 and not check_already_hit(col, right, enemyGrid):
       hitstack.append([col, right])

    # print("after appending: ", hitstack)
    col = chr(col + 65)
    return str(col) + str(row + 1)


def main():
    global turn
    playerGrid = make_ocean_grid()
    enemyGrid = make_ocean_grid()
    targetGrid = make_target_grid()
    enemyTargetGrid = make_target_grid()
    playerShips = make_ships()
    enemyShips = make_ships()
    winCondition = "none"
    turn = 0

    for ship in playerShips:
        place_ship(playerGrid, ship)

    for ship in enemyShips:
        place_ship(enemyGrid, ship)

    while winCondition == "none":
        if turn == 0:
            print("YOUR TURN.")
        elif turn == 1:
            print("IT'S THE ENEMY's TURN.")
        print_ocean_grid(enemyGrid) #
        print() #
        print_target_grid(targetGrid)
        print()
        print_ocean_grid(playerGrid)
        print()

        if turn == 0:
            coordinates_input = input("CALL A SHOT (A-J1-10): ")
            time.sleep(1)
            continue_message = input("INPUT TO SEE RESULT. ")
            call_shot(coordinates_input, enemyShips, enemyGrid, targetGrid, True)
            if len(enemyShips) == 0:
                winCondition = "player"
        elif turn == 1:

            time.sleep(1)
            continue_message = input("INPUT TO SEE RESULT. ")
            call_shot(hunt(playerGrid), playerShips, playerGrid, enemyTargetGrid, False)
            if len(playerShips) == 0:
                winCondition = "enemy"

        
        
        

    if winCondition == "player":
        print()
        print("YOU WON!", end="")
    elif winCondition == "enemy":
        print()
        print("YOU LOST!", end="")

if __name__ == "__main__":
    main()


