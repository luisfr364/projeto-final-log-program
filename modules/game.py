######
# Autores: Luis Fernando Farias Oliveira, Mário Gomes de Sousa Filho

from data.data import words, stickman_figure
from modules.os_interaction import OSInteraction
import random

class Game(): 

  #Inicialização das variáveis da classe
  def __init__(self):
    
    self.word = random.choice(words) #Seleção aleatória provinda da variável "words" do arquivo "data.py"
    
    self.guess_tries = 0 #Número de tentativas totais
    self.wrong_guesses = 0 #Número de tentativas incorretas
    self.win = False #Jogador venceu?

  #Método para começo do jogo
  def start(self):
    self.guess_engine()
      
  #Lógica dos palpites
  def guess_engine(self):
    letters_found = []
    
    found_letters_display_str = "" #String vazia para ser montadas, exibindo as letras encontradas ou "_" no lugar delas
    

    #Loop para continuar executando a lógica (para apenas quando o número de tentativas for maior do
    # que a quantidade de stickmans)
    while self.wrong_guesses < len(stickman_figure) - 1:
      OSInteraction().clear_terminal() #Limpa tudo no terminal
      print(stickman_figure[self.wrong_guesses])

      self.print_letters_and_check_win(letters_found, found_letters_display_str)
      if self.win: break
      
      found_letters_display_str = ""
      letter_input = input("Digite uma letra: ")

      if letter_input in self.word and letter_input not in letters_found:
        letters_found.append(letter_input)
      else:
        self.wrong_guesses += 1

      self.guess_tries += 1
    
    self.show_end_game()
      
  #Lógica para imprimir as palavras encontradas ou "_" para montar a string a ser printada
  def print_letters_and_check_win(self, letters_found, found_letters_display_str): 

    for char in self.word:
        if char in letters_found or char == " " or char == "-":
          found_letters_display_str += char
        else:
          found_letters_display_str += "_"

    print(f"\t{found_letters_display_str.upper()}")
    if found_letters_display_str == self.word:
      self.win = True
  
  def show_end_game(self):
    if self.win:
      print(f"Parabéns, você venceu o jogo!!!!\nForam necessárias {self.guess_tries} tentativas para você vencer :)")
    else: 
      print(stickman_figure[6])
      print(f"você perdeu :'(\nA palavra era: {self.word}")


