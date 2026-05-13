# 5. Number Guessing Game

secret = 42
guess  = int(input("Guess the number: "))

if guess == secret:
    print(" Correct! You guessed it!")
elif guess > secret:
    print(" Too High! Try lower.")
else:
    print(" Too Low! Try higher.")