import random

secret_number = random.randint(1,100)
# randint - chooses a random whole number

print("==============================")
print("     THE SECRET VAULT")
print("==============================")
print("A secret number is locked away.")
print("Crack the code before your chances run out!")
print("==============================")

# Note: The ==== lines are just decoration to make it look like a game.

player_name = input("Enter your name, agent: ")

print("\nChoose your security level:")
print("1. Easy - 10 attempts")
print("2. Medium - 7 attempts")
print("3. Hard - 5 attempts")

# I'm using `if`, elif, and else — To help my program make decisions.

difficulty = input("Select your level (1/2/3): ")
if difficulty == "1":
    attempts = 10
    print("Easy mode activated, agent!")
elif difficulty == "2":
    attempts = 7
    print("Medium mode activated. Stay sharp!")
elif difficulty == "3":
    attempts = 5
    print("Hard mode! No room for mistakes!")
else:
    attempts = 5
    print("Invalid choice. Hard mode has been selected!")  

    # I'm gonna use a WHILE LOOP bcz i don't want the program to stop. i want it to ask again. And again. Until the players wins or runs out of guesses.
while attempts > 0:
    guess = int(input("\nEnter Your Code: "))
    if guess == secret_number:
        print("Access granted! The vault is open!")
        break
    elif guess > secret_number:
        print("Too High! Bring your guess down.")
    else:
        print("Too Low! Aim higher")
attempts = attempts - 1
print("Attempts remaining:", attempts)  


if guess != secret_number and attempts == 0:
    print("Mission failed! The vault remains locked.")
    print("The secret number was:", secret_number)        

