# import random

# guessed_word_by_user = input("Enter a choice (rock, paper, scissors): ")
# winner_word = ["rock", "paper", "scissors"]
# winner_word = random.choice(winner_word)
# print(f"\nYou chose {guessed_word_by_user}, computer chose {winner_word}.\n")

# if guessed_word_by_user == winner_word:
#     print(f"Both players selected {guessed_word_by_user}. It's a tie!")
# elif guessed_word_by_user == "rock":
#     if winner_word == "scissors":
#         print("Rock smashes scissors! You win!")
#     else:
#         print("Paper covers rock! You lose.")
# elif guessed_word_by_user == "paper":
#     if winner_word == "rock":
#         print("Paper covers rock! You win!")
#     else:
#         print("Scissors cuts paper! You lose.")
# elif guessed_word_by_user == "scissors":
#     if winner_word == "paper":
#         print("Scissors cuts paper! You win!")
#     else:
#         print("Rock smashes scissors! You lose.")
import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")