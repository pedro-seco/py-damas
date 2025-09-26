JOGADOR_BRANCO = 0
JOGADOR_PRETO = 1
PRIMEIRO_QUADRANTE = 1
SEGUNDO_QUADRANTE = 2
TERCEIRO_QUADRANTE = 3
QUARTO_QUADRANTE = 4

jogador_preto = ""
jogador_branco = ""
jogador_vez = 0

letras = ["A","B","C","D","E","F","G","H"]
numeros = ["1","2","3","4","5","6","7","8"] 

pecas_imagens = { "0": " ⛀ ",       #Peça Branca no Quadrado Branco
                 "1": " ⛃ ",       #Rainha Branca no Quadrado Branco
                 "2": " ⛂ ",       #Peça Preta no Quadrado Branco
                 "3": " ⛃ ",       #Rainha Preta no Quadrado Branco
                 "4": "    ",       #Quadrado Branco Vazio
                 "10":"|⛀ |",      #Peça Branca no Quadrado Preto
                 "11":"|⛁ |",      #Rainha Branca no Quadrado Preto
                 "12":"|⛂ |",      #Peça Preta no Quadrado Preto
                 "13":"|⛃ |",      #Rainha Preta no Quadrado Preto
                 "14":"||||"        #Quadrado Preto Vazio
    }

pecas_texto = ["Peça Branca", "Rainha Branca", "Peça Preta", "Rainha Preta","Vazio"] #0,1,2,3,4
pecas_tiles = ["Quadrado Branco", "Quadrado Preto"] #0,10

def registra_jogadores() -> None:
    jogador_branco = input("> Jogador Branco (⛀ ), insira o nome que deseja usar: ")
    jogador_preto = input("> Jogador Preto (⛂ ), insira o nome que deseja usar: ")