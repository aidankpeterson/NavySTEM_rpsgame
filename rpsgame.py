from random import randint

p = ["Rock", "Paper", "Scissors"]

computer = p[randint(0,2)]

player = False

while player == False:
    print("Welcome To The Rock. Paper, Scissors Game!")
    player = input("Rock, Paper, Scissors?")
    print("Computer: " + computer)

    if computer == player:
        print("Tie Game! Close One!")

    elif player == "Rock":
        if computer == "Paper":
            print("You Lose :(", computer, "covers", player)
        else:
            print("You Win :)", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You Lose :(", computer, "shreds", player)
        else:
            print("You Win :)", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You Lose :(", computer, "smashes", player)
        else:
            print("You Win :)", player, "cuts apart", computer)
    else:
        print("Hmmm That Doesn't Work, Check Spelling And Try Again!")


    #player = False
    #computer = p[randint(0,2)]


