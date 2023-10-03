import csv # import da biblioteca que irá editar um arquivo csv
from datetime import datetime as dt # biblioteca que fornece data e hora
from os import * # biblioteca para manipular o cmd
from time import sleep 

def clear():
    sleep(1)
    system('cls')

class Entrevista:
    def __init__(self):
        self.idade = 1
        self.lista = []

    def create_csv(self):
        # Verifica se o arquivo já existe e se não está vazio
        if not path.isfile("saída.csv") or stat("saída.csv").st_size == 0:
            with open("saída.csv", "a", newline="", encoding="utf-8") as arquivo:
                w = csv.writer(arquivo)                
                w.writerow(['idade', 'genero', 'r1', 'r2', 'r3', 'r4', 'data'])

    def add_to_list(self, *args):
      for i in args:
        self.lista.append(i)
      return self.lista

    def add_to_csv(self):
       with open ("saída.csv", "a") as archive:
        w = csv.writer(archive)
        w.writerow(self.lista)

    def interview(self):
      while (True):  
          dados = []
          self.idade = int(input('Insira a idade do entrevistado (00 para encerrar o programa): '))
          if self.idade == 00:
            break

          gen = input('Insira o gênero do entrevistado: ')
          clear()
          
          r1 = input ('''1 - Qual o gênero de anime favorito do entrevistado?
          exs.:
          Shonen (Naruto, Dragon Ball), 
          Shoujo (Sailor Moon, Colégio Ouran Host Club),
          Seinen (Monster, Berserk)
          Josei (Usagi Drop). \n''')
          clear()
          
          r2 = input (''' Qual a produtora de anime favorita do entrevistado? 
          exs.:
          Ufotable - Franquia Fate, Kimetsu no Yaiba,
          Trigger - Little Witch Academia,
          Bones - Fullmetal Alchemist: Brotherhood, Boku no Hero Academia
          CloverWorks - The Promised Neverland,
          Wit Studio - Shingeki No Kyojin,
          Mappa - Jujutsu Kaisen, The God of High School,
          Toei - One Piece, Dragon Ball,
          Pierrot - Naruto,
          Production I.G - Kuroko no Basket. \n''')
          clear()
          
          r3 = input ('Há algum mangá que o entrevistado gostaria que fosse adaptado (ou re-adaptado) para anime?\n')
          clear()
          
          r4 = input ('''De qual forma o entrevistado costuma assistir anime?
                      (exs.: TV, Sites, Streaming)\n''')

          data = dt.now().strftime('%Y-%m-%d %H:%M:%S')
          interview = Entrevista()          
          interview.add_to_list(self.idade,gen,r1,r2,r3,r4,data)             
          interview.add_to_csv()

          clear()




if __name__ == "__main__":
  interview = Entrevista()
  interview.create_csv()
  interview.interview()
