import random

print("Welcome to the Number Gussing Game ")
print("I am thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty : Type 'easy' or 'hard' : ")

random_number = random.randint(1,101)
#print(random_number)

def guess_number():
    global random_number

    guess = int(input("Make a guess : "))
    if guess > random_number:
        print("Too High")

    elif guess < random_number:
        print("Too low")
        
    elif guess == random_number:
        print(f"You got it! The answer is {guess} .")
        exit()

    else:
        print("Guess again")
        
        

attempts_easy = 10
attempts_difficult = 5

if difficulty == "easy":
    for _ in range(10):
        print(f"You have {attempts_easy} attempts remaining to guess the number ")
        guess_number()
        attempts_easy -= 1
    if attempts_easy == 0:
        print("You've run out of guess. You lose")
        exit()
        
else:
    for _ in range(5):
        print(f"You have {attempts_difficult} attempts remaining to guess the number ")
        guess_number()
        attempts_difficult -= 1
    if attempts_difficult == 0:
        print("You've run out of guess. You lose")
        exit()

    
        

    
    
    
