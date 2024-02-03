from random import randrange

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


def check_boat(b, start,dire,take):
    
    dire = 1
    boat = []
    if dire == 1:
        for i in range(b):
            boat.append(start - i*10)
            boat = check_ok(boat,take)
    elif dire == 2:
        for i in range(b):
            boat.append(start - i*10)
            boat = check_ok(boat,take)    
    elif dire == 3:
        for i in range(b):
            boat.append(start - i*10)
            boat = check_ok(boat,take)   
    elif dire == 4:
        for i in range(b):
            boat.append(start - i*10)
            boat = check_ok(boat,take)       
    return boat

take = []
ships = []
boats = [5,4,3,3,2,2]
for b in boats:
    boat = [-1]
    while boat[0] == -1:
        boat_start = randrange(99)
        boat_direction = randrange (1,4)
        print(b,boat_start,boat_direction)
        boat = check_boat(b,boat_start,boat_direction,take)
    ships.append(boat)
    take = take + boat
    print(ships)