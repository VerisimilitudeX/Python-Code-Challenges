import random
import time

def waiting_game():
    """random time is created between 2 and 4 seconds and stored in a variable"""
    time.sleep(random.randint(2, 4))
    """random number is created between 1 and 10 and stored in a variable"""
    number = random.randint(1, 10)
    """user is prompted to enter a number between 1 and 10"""
    user_number = int(input("Enter a number between 1 and 10: "))
    """if user number is equal to random number, user wins"""
    if user_number == number:
        print("You win!")
    else:
        print("You lose!")

waiting_game()