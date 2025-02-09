from data import words, stickman_figure
import random


class Game(): 
  word = ""
  guess_tries = 0
  wrong_guesses = 0
  won = False

  def __init__(self):
    self.word = random.choice(words)
    self.guess_tries = 0
    self.wrong_guesses = 0

  def start(self):
    end = False
    while end == False:
      print("############## Jogo da forca V.1.0.0 ##############")
      
      print(f"a palavra é: {self.word}")
      
      self.guess_engine(end)
      

  def guess_engine(self,end):
    letters_found = []
    letters_and_sticks = ""
    while self.wrong_guesses < len(stickman_figure):
      print(self.wrong_guesses)
      print(stickman_figure[self.wrong_guesses])

      self.print_letters(letters_found, letters_and_sticks)
      letters_and_sticks = ""
      letter_input = input("Digite uma letra: ")

      if letter_input in self.word:
        letters_found.append(letter_input)
      else:
        self.wrong_guesses += 1

      ++self.guess_tries
      
  def print_letters(self, letters_found, letters_and_sticks): 
    for char in self.word:
        if char in letters_found:
          letters_and_sticks += char
        else:
          letters_and_sticks += "_"
    print(f"\t{letters_and_sticks.upper()}")
    
