import random
# This is a simple implementation of the Stone-Paper-Scissors game.

def get_user_choice():
    choices = ["rock", "stone", "paper", "scissors"]
    user_input = input("Enter your choice (rock or stone, paper, scissors): ").lower()
    while user_input not in choices:
        print("Invalid choice. Please try again.")
        user_input = input("Enter your choice (rock or stone, paper, scissors): ").lower()
    return user_input

# The computer randomly selects a choice from the list of options.
# The choices are "rock", "stone", "paper", and "scissors". The computer's choice is returned as a string.
# The computer's choice is determined by using the random.choice() function, which selects a random element from the list of choices.
def get_computer_choice():
    return random.choice(["rock", "stone", "paper", "scissors"])

# The determine_winner function takes the user's choice and the computer's choice as input and determines the winner of the game 
# based on the rules of Stone-Paper-Scissors. 
# The function returns a string indicating whether it's a tie, if the user wins, or if the computer wins.

# The rules of the game are as follows:
# - Rock (or Stone) beats Scissors
# - Paper beats Rock (or Stone)
# - Scissors beats Paper

# The function first checks if the user's choice and the computer's choice are the same, in which case it's a tie.
# Then it checks the combinations of choices to determine if the user wins or if the computer wins based on the rules of the game.
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" or user_choice == "stone") and (computer_choice == "stone" or computer_choice == "rock"):
        return "It's a tie!"
    elif (user_choice == "rock" or user_choice == "stone") and computer_choice == "scissors" or \
         (user_choice == "paper" and computer_choice == "rock" or computer_choice == "stone") or \
         (user_choice == "scissors" and computer_choice == "paper"):    
        return "You win!"
    else:
        return "Computer wins!"



# The play_game function manages the flow of the game. It keeps track of the user's score and the computer's score, 
# and it continues to play rounds until the user decides to stop. 
# After each round, it displays the current score and asks the user if they want to play again. 
# If the user chooses to stop, it thanks them for playing and ends the game.
def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        print(f"Current Score - You: {user_score}, Computer: {computer_score}")

        while True:       
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again in "yes":
                    break
            elif play_again in "no":
                print("Thanks for playing!")
                return
            else:
                print("invalid input. please enter yes or no.")
            
            
                

play_game()

