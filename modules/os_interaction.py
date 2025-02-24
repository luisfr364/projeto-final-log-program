###### Lógica de Programação ######
# Autores: Luis Fernando Farias Oliveira, Mário Gomes de Sousa Filho
import os

class OSInteraction():
    def clear_terminal(self):
      #Windows
      if os.name == 'nt':
        os.system('cls')
      #Unix-based
      else:
          os.system('clear')
