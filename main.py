from art import logo, vs
from game_data import data
import random
from replit import clear

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



def game(account_a, account_b, score, keep_playing):
  clear()
  print(logo)
  account_a= account_b
  account_b= select_element(data) 
  while account_a == account_b:
    account_b= select_element(data) 
    
  print("Compare A: " + format_element(account_a))
  print(vs)
  print("Against B: " + format_element(account_b))

  guess = input("Who more folowers? Type 'A' or 'B':")

  correct_guess = check_answer(guess, account_a, account_b) 
  print(correct_guess)
  if correct_guess:
    keep_playing = True
    score += 1
    message = f"You're right! Current score: {score}."
  else:
    keep_playing = False
    message = f"Sorry, that's wrong. Final score: {score}"

  print(message)
  return score



account_a= None
account_b= None

score = 0  
account_b= select_element(data)
keep_playing = True
while keep_playing:
  score = game(account_a, account_b, score, keep_playing)
  