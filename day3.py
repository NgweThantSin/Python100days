# print("Welcome to the python pizza deliveries.")
# size = input("What size pizza do you want? S,M orL: ")
# add_pepperoni = input("Do you want pepperoni? Y or N: " )
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# total = 0

# if size == "S":
#   total = 15
#   if add_pepperoni == "Y":
#     total += 2
#     if extra_cheese == "Y":
#       total += 1
#       print(f"Your final bill is : $ {total}.")
#     else:
#       print(f"Your final bill is : $ {total}.")


# elif size == "M":
#   total = 20
#   if add_pepperoni == "Y":
#     total += 3
#     if extra_cheese =="Y":
#       total += 1
#       print(f"Your final bill is : $ {total}.")
#     else:
#       print(f"Your final bill is $ {total}.")

# elif size == "L":
#   total = 25
#   if add_pepperoni == "Y":
#     total += 3
#     if extra_cheese == "Y":
#       total += 1
#       print(f"Your final bill is : $ {total}.")
#     else:
#       print(f"Your final bill is $ {total}.")


# else:
#   print("You are something wrong.")



# print("Welcome to the love calculator.")
# nam1 = input("What is your name?\n")
# nam2 = input("What is their name?\n")

# nam1_lower = nam1.lower()
# nam2_lower = nam2.lower()
# name_total = nam1_lower + nam2_lower

# t = name_total.count("t")
# r = name_total.count("r")
# u = name_total.count("u")
# e = name_total.count("e")

# total_true = t + r + u + e


# l = name_total.count("l")
# o = name_total.count("o")
# v = name_total.count("v")
# e = name_total.count("e")

# total_love = l + o + v + e

# true_love = int(str(total_true)+ str(total_love))

# if true_love < 10 or true_love > 90:
#   print(f"Your score is {true_love}, you go together like coke and mentos.")

# elif true_love < 50 and true_love > 40:
#   print(f"Your score is {true_love}, you are alright together.")

# else:
#   print(f"Your score is {true_love}.")




print("Welcome to the Treasure Island")
print("Your mission is to find the treasure.")
first = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'.")
second = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' for a boat. Type 'swim' to swim across.")
third = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")

if first == "left":
  if second == "wait":
    if third == "yellow":
      print("You win.")
    else:
      print("Game Over")
  else:
    print("Game Over.")


# else:
#   print("Game Over.")





