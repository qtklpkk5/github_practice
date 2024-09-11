
import random

def get_computer_choice(player_choice):
  if player_choice == "rock":
    return "paper"
  elif player_choice == "paper":
    return "scissors"
  else:
    return "rock"

def playGame():
  user_choice = input("Choose rock, paper, or scissors: ").lower()
  computer_choice = get_computer_choice(user_choice)
  print(f"Computer chose: {computer_choice}")

  if user_choice == computer_choice:
    return "It's a tie!"
  elif (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
    return "You win!"
  else:
    return "Computer wins!"

while True:
  play_best_of_three = input("Do you want to play best of 3? (yes/no): ").lower()
  if play_best_of_three in ("yes", "no"):
    break
  print("Invalid input. Please enter 'yes' or 'no'.")

if play_best_of_three == "yes":
  user_wins = 0
  computer_wins = 0
  while user_wins < 2 and computer_wins < 2:
    result = playGame()
    print(result)
    if result == "You win!":
      user_wins += 1
    elif result == "Computer wins!":
      computer_wins += 1
    print(f"Score: You {user_wins} - {computer_wins} Computer")
  if user_wins == 2:
    print("Congratulations! You won the best of 3!")
  else:
    print("Computer wins the best of 3! Better luck next time!")
else:
  print(playGame())
