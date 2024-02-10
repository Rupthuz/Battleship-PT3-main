def check_ok(boat,take):

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
            
    return boat

def create_ships():
    taken = []
    ships = []
    boats = [5,5,4,3,3,2]