row1 = [1, 2, 3]
row2 = [4,5,6]
row3 = [7,8,9]

def learning():    
    print(row1)

    print(row2)

    print(row3)

def hello():
    keep_playing = True 
    player = 0
    while keep_playing == True:
        if player % 2 == 0:
            player1 = input("X's turn to choose")
            player += 1
            learning()
        elif player % 2 == 1:
            player2 = input("O's turn to choose")
            player += 1
            learning()


def main():
    learning()
    hello()

main()