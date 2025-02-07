import random

data = [
    
    {
        'name' : 'Instagram',
        'follower_count' : 684,
        'description' : 'Social Media Platform',
        'country' : 'United States'
    },
    {   'name' : 'Cristiano Ronaldo',
        'follower_count' : 647,
        'description' : 'Professional Footballer',
        'country' : 'Portugal'
        
    },
    {
        'name' : 'Ariana Grande',
        'follower_count' : 377,
        'description' : 'Musician and actress',
        'country' : 'United States'
    },
    {
        'name' : 'Dwayne Johnson',
        'follower_count' : 395,
        'description' : 'Actor and professional wrestler',
        'country' : 'United States'
    },
    {
        'name' : 'Lionel Messi',
        'follower_count' : 505,
        'description' : 'Professional footballer',
        'country' : 'Argentine'
    },
    {
        'name' : 'Selena Gomez',
        'follower_count' : 423,
        'description' : 'Singer, actress and producer',
        'country' : 'American'
    },
    {
        'name' : 'Kylie Jenner',
        'follower_count' : 395,
        'description' : 'Enterpreneur, model and media personality',
        'country' : 'American'
    },
    {
        'name' : 'Kim Kardashian',
        'follower_count' : 360,
        'description' : 'Enterpreneur, model and media personality',
        'country' : 'American'
    },
    {   
        'name' : 'Beyonce',
        'follower_count' : 315,
        'description' : 'Singer, songwriter and actress',
        'country' : 'American'
        
    },
    {
        
        'name' : 'Khloe Lardashian',
        'follower_count' : 306,
        'description' : 'Enterpreneur and media personality',
        'country' : 'American'
    },
    {
        
        'name' : 'Justin Bieber',
        'follower_count' : 296,
        'description' : 'Musician',
        'country' : 'Canadian'
    },
    {
        
        'name' : 'Kendall Jenner',
        'follower_count' : 290,
        'description' : 'model and media personality',
        'country' : 'American'
    },
    {
        
        'name' : 'Taylor Swift',
        'follower_count' : 270,
        'description' : 'Musician',
        'country' : 'American'
    },
    {
        
        'name' : 'Virat Kohli',
        'follower_count' : 280,
        'description' : 'Cricketer',
        'country' : 'Indian'
    },
    {
        
        'name' : 'Jennifer Lopez',
        'follower_count' : 260,
        'description' : 'Musician and actress',
        'country' : 'American'
    },
    {
        
        'name' : 'Nicki Minaj',
        'follower_count' : 220,
        'description' : 'Musician',
        'country' : 'Trinidadian American'
    },
    {
        
        'name' : 'Neymar Jr',
        'follower_count' : 223,
        'description' : 'Professional Footballer',
        'country' : 'Brazilian'
    },
    {
        
        'name' : 'Miley Cyrus',
        'follower_count' : 207,
        'description' : 'Musician and actress',
        'country' : 'American'
    },
]
follower_count_a = 0
follower_count_b = 0
score = 0
should_continue = True
account_b = random.choice(data)


def format_account(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, {description} from {country}"



def check_answer(guess, follower_count_a, follower_count_b):
    if follower_count_a > follower_count_b:
        return guess == "a"
    else:
        return guess == "b"

while should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A : {format_account(account_a)}")
    print(f"Against B : {format_account(account_b)}")
    guess  = input("Who has more followers? : Type 'A' or 'B' : ").lower()

    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]

    is_correct = check_answer(guess, follower_count_a, follower_count_b)


    if is_correct :
        score += 1
        print(f"You are right. Current Score = {score} ")
    else:
        should_continue = False
        print(f"Sorry, That's wrong. Final Score = {score}")