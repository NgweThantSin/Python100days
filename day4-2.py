import random
your_choose = int(input("What do you choose? Type 0 for Rock, Type 1 for Paper or Type 2 for Scissors"))
if your_choose == 0:
    print("You choose Rock.")
elif your_choose == 1:
    print("You choose Paper.")
else:
    print("You choose Scissors.")
    

computer_choose = random.randint(0,2)
if computer_choose == 0:
    print("Computer choose Rock.")
elif computer_choose == 1:
    print("Computer choose Paper.")
else:
    print("Computer choose Scissors.")


if your_choose == 0 and computer_choose == 0:
    print("You are the same.")
elif your_choose == 0 and computer_choose == 1:
    print("You lose")
elif your_choose == 0 and computer_choose == 2:
    print("You Win.")
    
elif your_choose == 1 and computer_choose == 1:
    print("You are the same.")
elif your_choose == 1 and computer_choose == 0:
    print("You Win")
elif your_choose == 1 and computer_choose == 2:
    print("You Lose.")
    
    
elif your_choose == 2 and computer_choose == 2:
    print("You are the same.")
elif your_choose == 2 and computer_choose == 0:
    print("You Lose")
elif your_choose == 2 and computer_choose == 1:
    print("You Win")
else:
    print("something wrong.")