from modules.game import Game
import time
class GameHelper():

  def start_game(self):
    print("############## Jogo da forca V.1.1.0 ##############")
    time.sleep(0.5)
    print("\n\nTente acertar a palavra no número mínimo de tentativas")

    time.sleep(2)
    
    game = Game()
    game.start()

    self.game_finish()
    
    #Apenas para debug
    # print(f"a palavra é: {word}")
  
  def game_finish(self):
    should_continue = input("Deseja continuar? [s/n]: ")
    if should_continue == "s":
      self.start_game()
    
    return
    
