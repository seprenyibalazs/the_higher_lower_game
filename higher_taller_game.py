from gmae_data import celebrity
import random


score = 0
game_should_continue = True
account_b = random.choice(celebrity)

while game_should_continue:

    def format_data(account):
        account_name = account['name']
        account_description = account['description']
        account_from = account['from']
        return f"{account_name}, a {account_description}, {account_from}"

    def check_answer(guess, a_height, b_height):
        if a_height > b_height:
            return guess == "a"
        else:
            return guess == "b"

    account_a = account_b
    account_b = random.choice(celebrity)
    if account_a == account_b:
        account_b = random.choice(celebrity)

    print(f"Compare A: {format_data(account_a)}")
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who is highter? Type 'A' or 'B': ").lower()

    a_height_account = account_a['height']
    b_height_account = account_b['height']

    is_correct = check_answer(guess, a_height_account, b_height_account)

    if is_correct:
        score += 1
        print(f"You're right! Curremt score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
