from gmae_data import celebrity
import random


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


account_a = random.choice(celebrity)
account_b = random.choice(celebrity)
if account_a == account_b:
    account_b = random.choice(celebrity)

print(f"Compare A: {format_data(account_a)}")
print(f"Against B: {format_data(account_b)}")

guess = input("Who is highter? Type 'A' or 'B': ").lower()

a_height_account = account_a["height_count"]
b_height_account = account_b["height_count"]

is_correct = check_answer(guess, a_height_account, b_height_account)

if is_correct:
    print("You're right!")
else:
    print("Sorry, that's wrong.")
