def prime_checker(number):
        if number % 2 == 0 :
            if number % 4 ==  0:
                print("It is not a prime number.") 
            else:
                print("It is a prime number.")
        else:
            print("It is a prime number.")
         
             

n = int(input("Check this number: "))
prime_checker(number = n)