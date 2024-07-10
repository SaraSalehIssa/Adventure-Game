import random
import time


def user_choice(enemy, weapon):
    choices = [
        "1. To go to the house.",
        "2. To go to the cave."
    ]
    show_msg("\nPlease choose:")
    for choice in choices:
        show_msg(choice)
    show_msg("\nKindly enter your preferred action:")
    choice = is_valid(["1", "2"])
    if choice == "1":
        choice_1(enemy, weapon)
    else:
        weapon = choice_2(weapon)
        field(enemy, weapon)


def choice_1(enemy, weapon):
    show_msg(f"The {enemy} attacks you!")
    if weapon == "grenade":
        show_msg(f"You brace yourself for attack with {weapon}.")
        show_msg(f"However, the {enemy} runs away!")
        show_msg(f"Congratulations! You are won!")
    else:
        show_msg(f"The {enemy} is stronger than your {weapon}.")
        show_msg("Sorry! You are lost!")


def choice_2(weapon):
    if weapon == "grenade":
        show_msg(f"Before, you obtained the {weapon}.")
    else:
        weapon = "grenade"
        show_msg(f"In the cave, you found the {weapon}.")
        show_msg(f"You take the {weapon} with you.")
    return weapon


def field(enemy, weapon):
    show_msg(f"You run back into the field with {weapon}.")
    user_choice(enemy, weapon)


def replay():
    show_msg("****** END OF GAME ******")
    show_msg("\nWould you like to play once more? (yes/no)")
    choice = is_valid(["yes", "no"])
    if choice == "yes":
        show_msg("Welcome back!")
        start_the_game()
    else:
        show_msg("Goodbye!")


def start_the_game():
    enemy = random.choice(["goblin", "zombie", "alien"])
    weapon = random.choice(["knife", "Bow", "pistol"])
    show_msg(f"Please help us find the {enemy}")
    show_msg(f"In your hand you hold your {weapon}.")
    user_choice(enemy, weapon)
    replay()


def show_msg(msg):
    print(msg)
    time.sleep(1)


def is_valid(options):
    user_input = input().lower()
    while user_input not in options:
        show_msg(f"You must enter a valid input from {options}!")
        user_input = input().lower()
    return user_input


start_the_game()
