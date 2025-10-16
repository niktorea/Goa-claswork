import random

# generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("🎮 Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100...")

# loop until the player guesses correctly
while True:
    guess = int(input("Enter your guess: "))

    if guess != secret_number:
        print("WRONG ")
    else:
        print("🎉 Correct! You guessed the number!")
        break
