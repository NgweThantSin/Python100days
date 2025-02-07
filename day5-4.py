import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

random_letters = random.sample(letters,nr_letters)
random_numbers = random.sample(numbers,nr_numbers)
random_symbols = random.sample(symbols,nr_symbols)


password = [ ]
for n in random_letters:
    password.append(n)

for m in random_numbers:
    password.append(m) 
    
for o in random_symbols:
    password.append(o)


random.shuffle(password)
final_password = " "

for char in password:
    final_password += char
print(f"Your Password is {final_password}.")






    
