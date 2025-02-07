import random
hangman = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

word_list = ["ardvark", "baboon", "camel"]

display = []
chosen_word = random.choice(word_list)
print(chosen_word)
count = len(chosen_word)

while count > 0 :
    display.append("_")
    count -= 1 
#print(display)

end_of_game = False
lives = 6

while not end_of_game:

    guess = input("Guess a letter : ").lower()

#     # guess_list = []
#     # for letter in chosen_word:
#     #     guess_list.append(letter)
        
    c = len(chosen_word)


    for position in range(c):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        lives -=1
        if lives ==0 :
            end_of_game = True
            print("You Lose")
            
    print(f"{''.join(display)}")

        
    print(display)
        
    if "_" not in display:
        end_of_game = True
        print("You Win")
        
    print(hangman[lives])


      
          
              



        





    
 


