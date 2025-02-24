###### Lógica de Programação ######
# Autores: Luis Fernando Farias Oliveira, Mário Gomes de Sousa Filho

from tkinter import N
from modules.game import Game
import time
class GameHelper():

  def start_game(self, show_headers = True):
    if show_headers:
      print("############## Jogo da forca V.1.1.0 ##############")
      time.sleep(0.5)
      show_headers and print("\n\nTente acertar a palavra no número mínimo de tentativas")

      time.sleep(1.5)
    
    
    
    game = Game()
    game.start()

    self.game_finish()
    
  
  
  def game_finish(self):
    should_continue = input("\nDeseja continuar? [s/n]: ")
    if should_continue == "s":
      self.start_game(False)
    
    return
    
