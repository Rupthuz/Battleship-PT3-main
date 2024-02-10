from random import randrange
import random

def check_ok(boat, take):
    
    
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
        
    return ship,take

def create_ships():
    take = []
    ships = []
    boats = [5,5,4,3,3,2]
    
    for boat in boats:
        ship,take = get_ship(boat,take)
        ships.append(ship)
        
    return ships,take

def check_boat(b, start, dire, take):
    dire = 1
    boat = []
    if dire in [1, 2, 3, 4]:
        for i in range(b):
            boat.append(start - i * 10)
            boat = check_ok(boat, take)
    return boat

def create_boats():
    take = []
    ships = []
    boats = [5, 4, 3, 3, 2, 2]
    for b in boats:
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1, 5)
            boat = check_boat(b, boat_start, boat_direction, take)
        ships.append(boat)
        take.extend(boat)
    return ships, take

def game_board_comp(take):
    print("           Battleship Game          ")
    print("   0   1   2   3   4   5   6   7   8   9")
    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _  "
            if place in take:
                ch = " o  "
            row += ch
            place += 1
        print(x, row)

def getting_shot_comp(guesses,tactic):
    ok = "n"
    while ok == "n":
        try:
            if len(tactic) > 0:
                shot = tactic[0]
            shot = randrange(99)
            if shot not in guesses:
                ok = "y"
                guesses.append(shot)
                break
        except:
            print("Please entry again !")
    return shot, guesses

def game_board(hit, miss, comp):
    print("           Battleship Game          ")
    print("   0   1   2   3   4   5   6   7   8   9")
    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _  "
            if place in miss:
                ch = " x  "
            elif place in hit:
                ch = " o  "
            elif place in comp:
                ch = " 0  "
            row += ch
            place += 1
        print(x, row)

def check_hit(shot, ships, hit, miss, comp):
    
    missed = 0
    for i in range(len(ships)):
        if shot in ships[i]:
            ships[i].remove(shot)
            missed = 0
            if len(ships[i]) > 0:
                hit.append(shot)
                missed = 1
            else:
                comp.append(shot)
                missed = 2
    if missed == 0:
        miss.append(shot)
        
    return ships,hit,miss,comp,missed

def calc_tactic(shot,tactic,guesses,hit):
    
    temp = []
    if len(tactic) < 1:
        temp = [shot-1,shot+1,shot-10,shot+10]
    else:
        if shot-1 in hit:
            if shot-2 in hit:
                temp = [shot-3,shot+1]
            else:
                temp = [shot-2,shot+1]
        elif shot+1 in hit:
            if shot-2 in hit:
                temp = [shot+3,shot-1]
            else:
                temp = [shot+2,shot-1]
        elif shot-10 in hit:
            if shot-2 in hit:
                temp = [shot-30,shot+10]
            else:
                temp = [shot-20,shot+10]
        elif shot+10 in hit:
            if shot-2 in hit:
                temp = [shot+30,shot-10]
            else:
                temp = [shot+20,shot-10]
    
    cand = []
    for i in range(len(temp)):
        if temp[i] not in guesses and temp[i] < 100 and temp[i] > -1:
            cand.append(temp[i])
        random.shuffle(cand)
            
    return cand
                       
def check_if_empty(list_of_lists):
    return all([not elem for elem in list_of_lists])

hit = []
miss = []
comp = []
guesses = []
ships, take = create_boats()

tactic = []


for i in range(80):
    shot, guesses = getting_shot_comp(guesses,tactic)
    ships, hit, miss, comp, missed = check_hit(shot, ships, hit, miss, comp)
    
    if missed == 1:
        tactic = calc_tactic(shot,tactic,guesses,hit)    
    elif missed == 2:
        tactic = []
    elif len(tactic) > 0:
        tactic.pop(0)
        
        if check_if_empty(ships):
            print("Game Over",i)
            break
        
        
game_board_comp(take)   
game_board(hit, miss, comp)

