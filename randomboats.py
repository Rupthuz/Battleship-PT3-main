from random import randrange

def check_ok(boat, take):
    for num in boat:
        if num in take or num < 0 or num > 99:
            return [-1]
        elif num % 10 == 9 and boat.index(num) < len(boat) - 1:
            if boat[boat.index(num) + 1] % 10 == 0:
                return [-1]
    return boat


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


def getting_shot_comp(guesses):
    ok = "n"
    while ok == "n":
        try:
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
                ch = " @  "
            row += ch
            place += 1
        print(x, row)


def check_hit(shot, ships, hit, miss, comp):
    missed = 1
    for i in range(len(ships)):
        if shot in ships[i]:
            ships[i].remove(shot)
            missed = 0
            if len(ships[i]) > 0:
                hit.append(shot)
            else:
                comp.append(shot)
    if missed == 1:
        miss.append(shot)
    return ships, hit, miss, comp


hit = []
miss = []
comp = []
guesses = []
ships, take = create_boats()
game_board_comp(take)

for i in range(50):
    shot, guesses = getting_shot_comp(guesses)
    ships, hit, miss, comp = check_hit(shot, ships, hit, miss, comp)
    game_board(hit, miss, comp)
