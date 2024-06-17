import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
        return "Player wins"
    else:
        return "Computer wins"

def play_game():
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])
        print("Computer chooses:", computer_choice)

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "Player wins":
            player_score += 1
        elif result == "Computer wins":
            computer_score += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Player score:", player_score)
    print("Computer score:", computer_score)

play_game()