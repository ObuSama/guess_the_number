import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess!= random_number:
        guess = int(input(f'Guess a number between 1 and {x} :'))
        if guess < random_number:
            print("Sorry, guess again; the guess is low")
        if guess > random_number:
            print("Sorry, guess again, your guess is high")
    print(f"Yay! You have guess the number {random_number} right")

def computer_guess(x):
    low = 1
    high = x
    feedback =""
    while feedback!= 'C':
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess = low # could be high too
        feedback = input(f"Is the {guess} High(H), low(L) or Correct(C) ?")
        if feedback == 'H':
            high = guess-1
        if feedback =='L':
            low = guess+1
    print("Yay! I have guessed it right!")
        

if __name__ =="__main__":
    guess(10)
    print("Lets play another game. You choose a number between 1 and 100")
    computer_guess(100)