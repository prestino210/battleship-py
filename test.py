from main import make_ocean_grid
from main import make_target_grid
from main import print_ocean_grid
from main import make_ships
from main import place_ship
from main import call_shot
from main import hunt

def main():
    winCondition = False
    grid = make_ocean_grid()
    targetGrid = make_target_grid()
    ships = make_ships()
    turns = 0
    for ship in ships:
        place_ship(grid, ship)
    
    while winCondition == False:
        call_shot(hunt(grid), ships, grid, targetGrid, False)   
        if len(ships) == 0: 
           winCondition = True 
        print_ocean_grid(grid)
        turns += 1
           
    print_ocean_grid(grid)
    print(turns)
    
    
main()