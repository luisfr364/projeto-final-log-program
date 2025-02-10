from data import words, stickman_figure
import random

#OBS: Algumas partes do código possuem prints apenas para simples debug

class Game(): 
  #Palavra aleatoriamente escolhida do data.py
  word = ""
  #Número de tentativas totais
  guess_tries = 0
  #Número de tentativas incorretas
  wrong_guesses = 0
  #Jogador venceu?
  win = False

  #Inicialização das variáveis da classe
  def __init__(self):
    #Seleção aleatória provinda da variável "words" do arquivo "data.py"
    self.word = random.choice(words)
    

    self.guess_tries = 0
    self.wrong_guesses = 0

  #Método para começo do jogo
  def start(self):
    self.guess_engine()
      
  #Lógica dos palpites
  def guess_engine(self):
    #Letras da palavra encontradas pelo usuário
    letters_found = []
    #String vazia para ser montadas, exibindo as letras encontradas ou "_" no lugar delas
    letters_and_sticks = ""
    print(self.word)

    #Loop para continuar executando a lógica (para apenas quando o número de tentativas for maior do
    # que a quantidade de stickmans)
    #TODO implementar lógica de vitória
    while self.wrong_guesses < len(stickman_figure) - 1:
      print(self.wrong_guesses)
      print(stickman_figure[self.wrong_guesses])

      self.print_letters_and_check_win(letters_found, letters_and_sticks)
      if self.win: break
      
      letters_and_sticks = ""
      letter_input = input("Digite uma letra: ")

      if letter_input in self.word:
        letters_found.append(letter_input)
      else:
        self.wrong_guesses += 1

      self.guess_tries += 1
    
    self.show_end_game()
      
  #Lógica para imprimir as palavras encontradas ou "_" para montar 
  def print_letters_and_check_win(self, letters_found, letters_and_sticks): 
    #Para cada palavra e
    for char in self.word:
        if char in letters_found:
          letters_and_sticks += char
        else:
          letters_and_sticks += "_"

    print(f"\t{letters_and_sticks.upper()}")
    if letters_and_sticks == self.word:
      self.win = True
  
  def show_end_game(self):
    if self.win:
      print(f"Parabéns, você venceu o jogo!!!!\nForam necessárias {self.guess_tries} tentativas para você vencer :)")
    else: 
      print(stickman_figure[6])
      print(f"você perdeu :'(\nA palavra era: {self.word}")


  def end_game():
    TODO = True