import random

def getcomputerchoice():
    return random.choice(["rock", "paper", "scissors"])

def determinewinner(userchoice, computerchoice):
    if userchoice == computerchoice:
        return "tie"
    elif (userchoice == "rock" and computerchoice == "scissors") or \
         (userchoice == "scissors" and computerchoice == "paper") or \
         (userchoice == "paper" and computerchoice == "rock"):
        return "user"
    else:
        return "computer"

def displayresult(userchoice, computerchoice, winner):
    print(f"You chose: {userchoice}")
    print(f"Computer chose: {computerchoice}")
    if winner == "tie":
        print("The game has been tied!")
    elif winner == "user":
        print("You have winned the game!")
    else:
        print("You lost the game. Better luck next time.!")

def main():
    userscore = 0
    computerscore = 0

    print("Welcome to Rock-Paper-Scissors!")
    print("Instructions: Enter 'rock', 'paper', or 'scissors' to play.")
    print("Enter 'exit' to quit the game.")

    while True:
        userchoice = input("Enter your choice: ").lower()
        if userchoice == "exit":
            break
        if userchoice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computerchoice = getcomputerchoice()
        winner = determinewinner(userchoice, computerchoice)

        displayresult(userchoice, computerchoice, winner)

        if winner == "user":
            userscore += 1
        elif winner == "computer":
            computerscore += 1

        print(f"Score: You {userscore} - Computer {computerscore}")

        playagain = input("Do you want to play another round? (yes/no): ").lower()
        if playagain != "yes":
            break

    print("Thanks for playing! Final score:")
    print(f"You: {userscore} - Computer: {computerscore}")

main()
