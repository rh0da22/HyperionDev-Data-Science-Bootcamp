import random
# 1 = rock
# 2 = paper
# 3 = scissors

print("\n Welcome to a game of Rock, Paper, Scissors. You will be playing against the computer.\n")

games_won = 0
total_games = 1

while True:
    computer = random.randint(1, 3)

    while True:
        user = int(input("Enter 1 for Rock, 2 for Paper or 3 for Scissors: "))
        if user > 3 or user < 1:
            print("You have entered an invalid option. Please try again.")
        else:
            break

    if computer == 1 and user == 2:
        print("You won!")
        print("Paper covers Rock!")
        games_won += 1

    elif computer == 1 and user == 3:
        print("You lost!")
        print("Rock beats Scissors!")

    elif computer == 2 and user == 1:
        print("You lost!")
        print("Paper covers Rock!")

    elif computer == 2 and user == 3:
        print("You lost!")
        print("Scissors cuts Paper!")

    elif computer == 3 and user == 1:
        print("You won!")
        print("Rock beats Scissors!")
        games_won += 1

    elif computer == 3 and user == 2:
        print("You won!")
        print("Scissors cuts Paper!")
        games_won += 1

    elif computer == user:
        print("It's a tie!")
    
    else:
        print("This statement will never print (hopefully!)")

    play_again = input("Would you like to play again? Enter 'y' for yes or anything else for no: ").lower()

    if play_again == "y":
        total_games += 1
        continue
    else:
        print("Hope you had fun.")
        break

print(f"You won {games_won} games out of {total_games}.")

