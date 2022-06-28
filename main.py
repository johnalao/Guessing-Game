import random
from arts import logo
print(logo)

easy_lives = 10
hard_lives = 7


def start():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   difficulty_case = difficulty.lower
  if difficulty == "easy":
    return easy_lives
  else:
    return hard_lives

    
def check_answer(guess, computer_choice, lives):
  """Checks answer and number of attempts remaining"""
  if guess > computer_choice:
    print("Too High")
    return lives - 1
  elif guess < computer_choice:
    print("Too low")
    return lives - 1 
  else:
    print(f"You've got it right. the answer was {computer_choice}")
    
def game():
  print("Welcome to the Number Guessing Game!")
  print("I am thinking of a number between 1 and 100.")
  computer_choice = random.randint(1, 100)
  print(f"The chosen word is {computer_choice}")
  lives = start()
  guess = 0
  while guess != computer_choice:
    print(f"You have {lives} number/s of attempt remaining")
    guess = int(input("Make a Guess: "))
    lives = check_answer(guess, computer_choice, lives)
    if lives == 0:
      print("You've ran out of attempts, you lose.")
      return
    


game()

  


