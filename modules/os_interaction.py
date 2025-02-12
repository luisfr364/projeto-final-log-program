import os

class OSInteraction():
    def clear_terminal(self):
      #Windows
      if os.name == 'nt':
        os.system('cls')
      #Unix-based
      else:
          os.system('clear')
