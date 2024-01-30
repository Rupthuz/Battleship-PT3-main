# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high



def getting_shot():
    
    ok = "n"
    while ok == "n":
        try:
            shot = input("Please enter your guess number !")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("Please enter a valid number !")
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
    
    
miss = [20,45,50]
hit = [10,25,33]
comp = [43,6]


shot = getting_shot()
game_board(miss,hit,comp)