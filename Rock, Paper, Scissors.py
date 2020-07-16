from random import randint


e=['Rock','Paper','Scissors']  # making a list of the
computer=e[randint(0,2)]       # the computer is generating from the list
player=False        # making player variable is false


while player==False:        # player always = false so this part always runs
    player=input("Rock,Paper,Scissors?")
    if player==computer:
        print("Tie!")
    elif player=="Rock":
        if computer=="paper":
            print ("The computer chose", computer)
            print ()
            print("You lose!",computer,"covers",player)
        else:
            print("The computer chose", computer)
            print ()
            print("You win!",player,"smashes",computer)
    elif player=="Paper":
        if computer=="Scissors":
            print("The computer chose", computer)
            print ()
            print("You lose!",computer,"cut",player)
        else:
            print("The computer chose", computer)
            print ()
            print("You win!",player,"covers",computer)
    elif player=="Scissors":
        if computer=="Rock":
            print("The computer chose", computer)
            print ()
            print("You lose...",computer,"smashes",player)
        else:
            print("The computer chose", computer)
            print ()
            print("You win!",player,"cut",computer)
    else:
        print("That's not a valid play.Check your spelling!")

   # player=False                # this reruns the code over and over again
   # computer=e[randint(0,2)]

