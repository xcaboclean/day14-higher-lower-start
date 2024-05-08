from art import logo, vs
from game_data import data
import random

def select_element(data):
  element = random.choice(data)
  return element

def format_element(element):
  show_element = element['name'] + ", "+ element['description']+", from "+ element['country']+"."
  return show_element

print(logo)
account_a= format_element(select_element(data))
account_b= format_element(select_element(data))
print("Compare A: " + account_a)
print(vs)
print("Against B: " + account_b)
account_b= format_element(select_element(data))