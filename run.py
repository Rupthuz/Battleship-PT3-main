# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


def getting_shot(guesses):
    
    ok = "n"
    while ok == "n":
        try:
            shot = input("Please enter your guess number !")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("Please enter a valid number !")
            elif shot in guesses: 
                print("Number used before !") 
            else:
                ok = "y"
                break
        except:
            print("Please entry again !")
    return shot

def game_board(hit,miss,comp):
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
            row = row + ch
            place = place + 1
        print(x, row)

def check_hit(shot,boat1,boat2,hit,miss,comp):
     
    if shot in boat1:
        boat1.remove(shot)
        if len(boat1) > 0:
             hit.append(shot)
        else:
            comp.append(shot)
    else:
         miss.append(shot)
    if shot in boat2:
        boat2.remove(shot)
        if len(boat2) > 0:
             hit.append(shot)
        else:
            comp.append(shot)
    else:
         miss.append(shot)
         
    return boat1,boat2,hit,miss,comp
     
     
boat1 = [45,46,47]
boat2 = [2,22,25]
miss = []
hit = []
comp = []

for i in range(10):
    guesses = hit + miss + comp
    shot = getting_shot(guesses)
    boat1,boat2,hit,miss,comp = check_hit(shot,boat1,boat2,hit,miss,comp)
    game_board(miss,hit,comp)
    
    if len(boat1) < 1 and len(boat2) < 1:
        print("You Won !")
        break
print("End Game")