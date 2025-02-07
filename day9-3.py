def clear():
    "Terminal : Clear"
    
blind_auction = {}

def highest_bidder(bidder_record):
    highest = 0
    winner = ""
    for bidder in bidder_record:
        score = bidder_record[bidder]
        if score > highest:
            highest = score
            winner = bidder
    print(f"Winner is {winner} with ${highest}")
    


loop = False
while not loop:

    name = input("What is your name?")
    bid = int(input("What is your bid? $"))
    blind_auction[name] = bid
    other_bidder = input("Are there any other bidders? Type yes or no")
    if other_bidder == "no":
        loop = True
        highest_bidder(blind_auction)
    elif other_bidder == "yes":
        clear()
        
    
    
    
    

