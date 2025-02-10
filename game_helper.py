from game import Game

class GameHelper():

  def start_game(self):
    print("############## Jogo da forca V.1.0.0 ##############")
    print("\nTente acertar a palavra no número mínimo de tentativas")
    
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
    
