from art import logo, vs
from game_data import data
import random

def select_element(data):
  element = random.choice(data)
  return element

def format_element(element):
  show_element = element['name'] + ", "+ element['description']+", from "+ element['country']+"."
  return show_element

def check_answer(guess, account_a, account_b):

  if account_a['follower_count'] > account_b['follower_count']:
    bigguer = 'A'
  elif account_a['follower_count'] < account_b['follower_count']:
    bigguer = 'B'
  return (guess == bigguer)


score = 0  
print(logo)
account_a= select_element(data)
account_b= select_element(data)
print("Compare A: " + format_element(account_a))
print(vs)
print("Against B: " + format_element(account_b))

guess = input("Who more folowers? Type 'A' or 'B':")

correct_guess = check_answer(guess, account_a, account_b) 

if correct_guess:
  score += 1
  print(f"You're right! Current score: {score}.")
else:
  print(f"Sorry, that's wrong. Final score: {score}")
