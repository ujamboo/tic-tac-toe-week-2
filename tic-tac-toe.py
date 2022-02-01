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
            player1 = int(input("X's turn to choose "))
            for num in row1:
                if num == player1:
                    num = "x"
            for num in row2: 
                if num == player1:
                    num = "x"
            for num in row3:
                if num == player1:
                    num = "x"
        
            player += 1
            learning()
        elif player % 2 == 1:
            player2 = input("O's turn to choose ")
            for num in row1:
                if num == player2:
                    num = "o"
            for num in row2:
                if num == player2:
                    num = "o"
            for num in row3:
                if num == player2:
                    num = "o"

            player += 1       
            learning()


def main():
    learning()
    hello()

main()

def next_step():
    pass