# import random
# random_number = random.randint(0,1)
# if random_number == 1:
#     print("Head")
# else:
#     print("Tails")



import random
names_string = input("Give me everybody's names, separated by comma.")
names = names_string.split(",")
x = len(names)

random_names = random.randint(0,x-1)

person_who_will_pay_bill = names[random_names]
print(f"{person_who_will_pay_bill} is going to pay the bill today.")