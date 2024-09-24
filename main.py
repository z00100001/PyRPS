import random

count = 0
choices = ["Rock", "Paper", "Scissors"]


def game_start():
    global count
    winrate = 0
    ai_choice = random.randint(0, 2)
    ai_choice_str = choices[ai_choice]

    print("What is your choice? (Rock, Paper, Scissors)")
    user_choice = input()

    while user_choice not in choices:
        print("Invalid choice. Please select Rock, Paper, or Scissors.")
        user_choice = input()

    print("AI chose {}".format(ai_choice_str))

    if user_choice == ai_choice_str:
        print("Tie!")
    elif (user_choice == "Rock" and ai_choice_str == "Scissors") or \
            (user_choice == "Paper" and ai_choice_str == "Rock") or \
            (user_choice == "Scissors" and ai_choice_str == "Paper"):
        print("You Won!")
        winrate = 1  # Increase winrate only when user wins
    else:
        print("AI Won!")

    count += 1
    print("You played {} times so far".format(count))
    if count > 0:
        print("You have a win percentage of {:.2f}%".format((winrate / count) * 100))
    game_start()


game_start()
