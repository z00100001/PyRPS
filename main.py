import random

count = 0
choices = ["rock", "paper", "scissors"]


def game_start():
    global count
    winrate = 0
    ai_choice = random.randint(0, 2)
    ai_choice_str = choices[ai_choice]

    print("What is your choice? (Rock, Paper, Scissors)")
    user_choice = input().lower()

    while user_choice not in choices:
        print("Invalid choice. Please select Rock, Paper, or Scissors.")
        user_choice = input().lower()

    print("AI chose {}".format(ai_choice_str))

    if user_choice == ai_choice_str:
        print("Tie!")
    elif (user_choice == "rock" and ai_choice_str == "scissors") or \
            (user_choice == "paper" and ai_choice_str == "rock") or \
            (user_choice == "scissors" and ai_choice_str == "paper"):
        print("You Won! Thank you for playing!")
        winrate = 1 
    else:
        print("AI Won!")

    count += 1
    print("You played {} times so far".format(count))
    if count > 0:
        print("You have a win percentage of {:.2f}%".format((winrate / count) * 100))
    game_start()


game_start()
