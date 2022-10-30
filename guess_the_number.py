import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess!= random_number:
        guess = int(input(f'Guess a number between 1 and {x} :'))
        if guess < random_number:
            print("Sorry, guess again; the guess is low")
        elif guess > random_number:
            print("Sorry, guess again, your guess is high")
    print(f"Yay! You have guess the number {random_number} right")


if __name__ =="__main__":
    guess(10)