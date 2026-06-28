import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user = input("\n Choose Rock, Paper, or Scissors: ").lower()
        if user in choices:
            return user
        else:
            print(" Invalid choice! Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user, computer, result):
    print(f"\n You chose: {user.capitalize()}")
    print(f" Computer chose: {computer.capitalize()}")

    if result == "tie":
        print(" It's a Tie!")
    elif result == "user":
        print(" You Win!")
    else:
        print(" Computer Wins!")

def play_game():
    user_score = 0
    computer_score = 0

    print(" Welcome to Rock, Paper, Scissors Game!")
    print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock.")

    while True:
        user = get_user_choice()
        computer = get_computer_choice()

        result = determine_winner(user, computer)
        display_result(user, computer, result)

        # Score update
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        print(f"\n Score -> You: {user_score} | Computer: {computer_score}")

        # Play again option
        again = input("\n Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("\nThanks for playing!")
            print(f" Final Score -> You: {user_score} | Computer: {computer_score}")
            break

# Run the game
if __name__ == "__main__":
    play_game()