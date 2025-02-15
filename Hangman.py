
''' This is my (Dr. Gibson's) version. Thank you to Sherine, Niko, & Alicia for debugging :)'''

import random
from IPython.display import clear_output
sowpods = "sowpods.txt"
#words from http://norvig.com/ngrams/sowpods.txt

#creating a function to generate a random word each round
def word_generator():
  filename = sowpods
  f = open(filename, "r", encoding="utf8")
  words = f.readlines()
  f.close()

  return random.choice(words).strip()

answer = word_generator()

#creating the opening & instructions to the game
def opening():
  print("Welcome to Hangman! You will have six guesses to correctly guess a randomly generated word")
  print("Your word is")
  create_board()

#creating the blank spaces for the player
def create_board():
  global answer_list #making this global so I can access it in other functions
  answer_list= []
  answer_list.extend(answer) #turning the random word into a list of characters

  guess_board = []
  x = 1
  while x <= len(answer_list):
    guess_board.append("__") #creating a blank spot for each character
    x += 1
  print(guess_board)

#creating the system to judge if an answer is right or wrong
def guesses():
  tries = 6
  tried_letters = [] #stores all letters attempted
  found_letters = [] #stores all correct answers
  found_board = list('_' * len(answer_list)) #creates copy of the answer list
  while tries != 0:
    guess = input("What letter would you like to try?").upper()

    if guess.isalpha():
      if guess in found_letters:
        print(f"You've already found {guess}!")
      elif guess in tried_letters:
        print(f"You've already tried {guess}. It's not in the word!")
      elif guess in answer:
        print(f"Success! {guess} is in the word.")
        found_letters.append(guess) #adding any successful letter to the list

        for pos, x in enumerate(answer_list):

          if x == guess: #if a letter is in the list
            y = answer_list.index(x) #finding the index of that letter
            found_board[pos] = x #replacing that __ spot with the letter
        print(found_board) #print the current board

        if found_board == answer_list:
          print(f"You won! The word was {answer}")
          decision = input("Would you like to play again? (Y/N)").upper()
          if decision == "Y":
            clear_output()
            game_play()
          else:
            break

      else:
        print(f"Sorry, there is no {guess} in the word.")
        tried_letters.append(guess)
        tries = tries - 1
        print(f"You have {tries} tries left")
        if tries == 0:
          print(f"You lost the game! The word was {answer}")
          decision = input("Would you like to play again? (Y/N)").upper()
          if decision == "Y":
            clear_output()
            game_play()
          else:
            break

    else:
      print("That wasn't a letter. Try again!")
      guess = input("What letter would you like to try?")

#packaging all this in a single function for ease of use
def game_play():
  word_generator()
  opening()
  guesses()

game_play()
