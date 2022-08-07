print("rock ,paper and scissors game and the players are john and bob")

again='y'
while (again == 'y'):

    john=input("john --> rock, paper, or scissors? ")
    bob=input("bob --> rock, paper, or scissors? ")

    if john=="rock":
        if bob=="rock":
            print("game is drawn")
        elif bob=="paper":
            print("john won the game")
        elif bob =="scissors":
            print("john won the game") 
    elif john=="paper":
        if bob=="rock":
            print("bob won the game")
        elif bob=="paper":
            print("game is drawn")
        elif bob =="scissors":
            print("bob won the game")          
    elif john=="scissors":
        if bob=="rock":
            print("bob won the game")
        elif bob=="paper":
            print("john won the game ")
        elif bob =="scissors":
            print("game is drawn")   
    else:
        print("your choice is invalid") 

    again=input("type'y' if you want to play again:")                     



   