def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide (n1 , n2):
    return n1 / n2

operation =  {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    num1 = float(input("What is the first number? : "))
    # num2 = float(input("What is the second number? : "))
    for operator in operation:
        print(operator)
        
    loop = True
    while loop:    

        
        ask = input("Pick an operation : ")
        num2 = float(input("What is the next number? : "))

        chose_operator = operation[ask]   
        answer = chose_operator(num1,num2)

        print(f"{num1} {ask} {num2} =  {answer}")

        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit : " )
        
            
        if should_continue == "y" :
            loop = True
            num1 = answer
                
        else:
            loop = False
            calculator()
                
calculator()







