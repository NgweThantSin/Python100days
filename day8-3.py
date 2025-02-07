
#we can write with only one function just below.
    
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
        
    print(f"Here is the {direction}d result: {end_text}")
    
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    
    if result == "no":
        should_continue = False
        print("Goodbye")




should_continue = True
while should_continue:
    
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']
    direction = input("Type 'encode' to encrypt and type 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    
    
    shift %= 24         
    caesar(start_text = text , shift_amount = shift, cipher_direction = direction  )

    
    



# def encrypt(plain_text, space_shift):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encrypted text is {cipher_text}")



# def decrypt(plain_text, space_shift):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The decrypted text is {cipher_text}")
        
        
# if direction == "encode":
#     encrypt(plain_text = text , space_shift = shift )
# else:
#     decrypt(plain_text = text , space_shift = shift )
        


    
    
        
