from random import randrange

def check_boat(b, start,dire):
    
    dire = 1
    boat = []
    if dire == 1:
        for i in range(b):
            boat.append(start - i*10)
            print(start - i*10)
    elif dire == 2:
        for i in range(b):
            boat.append(start - i*10)
            print(start - i*10)    
    elif dire == 3:
        for i in range(b):
            boat.append(start - i*10)
            print(start - i*10)   
    elif dire == 4:
        for i in range(b):
            boat.append(start - i*10)
            print(start - i*10)   

boats = [4]
for b in boats:
    boat_start = randrange(99)
    boat_direction = randrange (1,4)
    print(b,boat_start,boat_direction)
    check_boat(b,boat_start,boat_direction)