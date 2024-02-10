def check_ok(boat,take):

    boat.sort()
    for i in range(len(boat)):
        num = boat[i]
        if num in take:
            boat = [-1]
            break
        elif num < 0 or num > 99:
            boat = [-1]
            break
        elif num % 10 == 9 and i < len(boat)-1:
            if boat[i+1] % 10 == 0:
                boat = [-1]
                break
        if i != 0:   
            if boat[i+1] != boat[i]+1 and boat[i+1] != boat[i]+10:
             boat = [-1]
             break
         
    return boat

def get_ship(long,take):
    
    ok = True
    while ok:
        ship = []
        print("Enter your Ship Lenght", long)
        for i in range(long):
            boat_num = input("Please enter a number")
            ship.append(int(boat_num))
            
        ship = check_ok(ship,take)
        if  ship[0] != -1:  
            take = take + ship
            break
        else:
            print("error, Please enter the number again !")    
        
    return ship

def create_ships():
    take = []
    ships = []
    boats = [5,5,4,3,3,2]
    
    for boat in boats:
        ship,take = get_ship(boat,take)
        ships.append(ship)
        
    return ships,take

ships = create_ships()