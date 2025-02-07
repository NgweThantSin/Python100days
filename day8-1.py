test_h = int(input("Height of wall :"))
test_w = int(input("Width of wall : "))
coverage = 5

def paint_calc(height, width, cover):
    num_of_cans = round((height * width ) / 5)
    
    #you can use the below instruction instead of round function.
    #import math
    #num_of_cans = math.ceil(area/cover)
    
    print(f"You will need {num_of_cans} of paint.")

paint_calc(height = test_h, width = test_w, cover = coverage)

