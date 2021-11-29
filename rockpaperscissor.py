from random import randrange
while True:
    game_rule = ["rock", "paper", "scissor"]
    your_act = input("please enter 0: rock, 1:paper, 2:scissor -->")
    your_act = game_rule[int(your_act)]
    print("you: %s" %your_act)


    computer_act = game_rule[int(randrange(3))]
    print("computer: %s" % (computer_act))

    if your_act=="scissor"and computer_act=="paper":
        print("I win!")
        break 
    if your_act=="rock"and computer_act=="scissor":
        print("rock wins!")
        break 
    if your_act=="paper" and computer_act=="rock":
        print("I always win!")
        break  
    ##if computer_act win or draw:    
        
    if your_act=="scissor" and computer_act=="rock":
        print("lose")
        continue
    if your_act=="scissor" and computer_act=="scissor":
        print("Tie")
        continue
    if your_act=="rock" and computer_act=="rock":
        print("again")
        continue
    if your_act=="rock" and computer_act=="paper":
        print("try again")
        continue
    if your_act=="paper"and computer_act=="scissor":
        print("go home")
        continue
    if your_act=="paper" and computer_act=="paper":
        print("that is no fair")
        continue



