import random
def guessgame():
    secretNumber = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Enter a number between 1 and 100: "))
            attempts += 1
            if guess < secretNumber:
                print("Too low!")
            elif guess > secretNumber:
                print("Too high!")
            else:
                print(f"You guessed it! In the attempt {attempts}")
                break
        except ValueError:
            print("Please set a integer number.")
guessgame()