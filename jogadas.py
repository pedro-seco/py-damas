#----------Imports----------
import tabuleiro as tb

#----------Variáveis Globais----------
jogador = 0
diagonaisDireitas = []
diagonaisEsquerda = []
diagonaisFatiadas = []
diagonaisBooleanas = ""
diagonal = []
origem = ""
destino = ""

#----------Manipulação do Tabuleiro----------
def acessaTile(tile, i = 0, j = 0):
    index = retornaIndex(tile)
    linha = index[0]
    coluna = index[1]

    return tb.tabuleiro[linha+i][coluna+j]

def calcDist(q1,q2): 
    return [retornaIndex(q2)[0] - retornaIndex(q1)[0],retornaIndex(q2)[1] - retornaIndex(q1)[1]]

def retornaIndex(tile):
    letras = "ABCDEFGH"
    coluna = letras.find(tile[0])
    linha = int(tile[1])-1

    return [linha,coluna]

#----------Condicionais----------

def isVazio(tile):
    booleano = False
    if acessaTile(tile)[2] == "Vazio":
        booleano = True
    return booleano

def isBranco(tile):
    booleano = False
    if acessaTile(tile)[2] == "Peça Branca" or acessaTile(tile)[2] == "Rainha Branca":
        booleano = True
    return booleano

def isPreto(tile):
    booleano = False
    if acessaTile(tile)[2] == "Peça Preta" or acessaTile(tile)[2] == "Rainha Preta":
        booleano = True
    return booleano

def isDama(tile):
    booleano = False
    if acessaTile(tile)[2] == "Rainha Branca" or acessaTile(tile)[2] == "Rainha Preta":
        booleano = True
    return booleano

def isQuadrado(lista):
    booleano = False
    if abs(lista[0]) == abs(lista[1]):
        booleano = True
    return booleano

def isEsquerdaDireita(origem,destino):
    direcao = calcDist(origem,destino)
    booleano = False

    if direcao[0] + direcao[1] == 0: #True = Esquerda, False = Direita
        booleano = True
    return booleano

def isStringZero(lista):
    booleano = True

    for i in lista:
        if i != "0":
            booleano = False
    
    return booleano

#----------Diagonais----------
def criaDiagonais(tile):
    global diagonaisEsquerda        
    global diagonaisDireitas
    global diagonaisFatiadas

    diagonaisDireitas = []
    diagonaisEsquerda = []
    diagonaisFatiadas = []

    for linha in range(8):
        for coluna in range(8):
          direcao = calcDist(tile, tb.tabuleiro[linha][coluna][0])
          if tb.tabuleiro[linha][coluna][0] == tile:
                  diagonaisEsquerda.append(tb.tabuleiro[linha][coluna][0])
                  diagonaisDireitas.append(tb.tabuleiro[linha][coluna][0])

          elif isQuadrado(direcao):
              if isEsquerdaDireita(tile,tb.tabuleiro[linha][coluna][0]):
                  diagonaisEsquerda.append(tb.tabuleiro[linha][coluna][0])
              else:
                  diagonaisDireitas.append(tb.tabuleiro[linha][coluna][0])

def boolDiagonal(lista):
    global diagonaisBooleanas
    diagonaisBooleanas = ""
    for tile in lista:
        if isVazio(tile):
            diagonaisBooleanas += "1"
        else:
            diagonaisBooleanas += "0"

def direcaoDiagonal(origem,destino):
    global diagonal
    if isEsquerdaDireita(origem,destino):
        diagonal = diagonaisEsquerda
    else:
        diagonal = diagonaisDireitas
    
def tamanhoDiagonal(origem,destino):
    global diagonal

    inicio = 0
    fim = 0 
    for item in diagonal:
        if item == origem:  
            inicio = diagonal.index(origem)
            break
    
    for item2 in diagonal:
        if item2 == destino:
            fim = diagonal.index(destino)
            break

    diagonal = diagonal[min(inicio,fim):max(inicio,fim)+1]

def fatiaDiagonais(tile,lista):
    for item in range(len(lista)):
            if tile == lista[item]:
                diagonaisFatiadas.append(lista[item+1:])
                diagonaisFatiadas.append(lista[:item])


def moldaDiagonal(origem,destino):
    global diagonal
    criaDiagonais(origem)
    direcaoDiagonal(origem,destino)
    tamanhoDiagonal(origem,destino)
    fatiaDiagonais(origem,diagonaisDireitas)
    fatiaDiagonais(origem,diagonaisEsquerda)

#----------Definição das jogadas----------
def defineJogada(jogada):
    global origem
    global destino
    origem = jogada[:2]
    destino = jogada[3:]
    moldaDiagonal(origem,destino)

    if isDama(origem) == False:
        jogadaPeca(origem,destino)
    
    elif isDama(origem) == True:
        jogadaRainha(origem,destino)

def comeMais(tile):
    booleano = False
    jogadaValida = "10"
    fatiaDiagonais(tile,diagonaisDireitas)
    fatiaDiagonais(tile,diagonaisEsquerda)

    #preciso transformar os dados que vem em uma "string booleana"
    #lista -> "10" ou lista -> "11010 por ex

    for lista in diagonaisFatiadas:
        boolDiagonal(lista)

        if diagonaisBooleanas[:2] == jogadaValida:
            if isBranco(tile) and isPreto(lista[1]):
                booleano = True
            
            elif isPreto(tile) and isBranco(lista[1]):
                booleano = True
        
        elif isDama(tile):
            for i in range(len(lista)):
                if jogadaValida in lista and isStringZero(lista[:lista.index(jogadaValida)]):
                    if isBranco(tile) and isPreto(lista[lista.index(jogadaValida)]):
                        booleano = True

                    elif isPreto(tile) and isBranco(lista[lista.index(jogadaValida)]):
                        booleano = True

    return booleano

def procuraPromo(jogador):
    
    if jogador == 0:
        for coluna in range(8):
            if tb.tabuleiro[0][coluna][2] == "Peça Branca":
                tb.tabuleiro[0][coluna][2] = "Rainha Branca"

    elif jogador == 1:
        for coluna in range(8):
            if tb.tabuleiro[7][coluna][2] == "Peça Preta":
                tb.tabuleiro[7][coluna][2] = "Rainha Preta"

#----------Jogadas----------
def movePeca(origem,destino):
    acessaTile(destino)[2] = acessaTile(origem)[2]
    acessaTile(origem)[2] = "Vazio"

def comePeca(origem,destino): 
    acessaTile(diagonal[-2])[2] = "Vazio" 
    movePeca(origem,destino)

def jogadaRainha(origem, destino):
    global jogador
    jogadaValida = "10"
    boolDiagonal(diagonal)
    
    if jogadaValida in diagonaisBooleanas and isStringZero(diagonaisBooleanas[:diagonaisBooleanas.index(jogadaValida)]):
        if isBranco(origem) and isPreto(diagonal[diagonaisBooleanas.index(jogadaValida)+1]):
            comePeca(origem,destino)
            if comeMais(destino):
                jogador = 0
            else:
                jogador = 1

        elif isPreto(origem) and isBranco(diagonaisBooleanas[diagonaisBooleanas.index(jogadaValida)]):
            comePeca(origem,destino)
            if comeMais(destino):
                jogador = 1
            else:
                jogador = 0
    
    elif not all(diagonal) and isVazio(destino):
        if isBranco(origem):
            movePeca(origem,destino)
            jogador = 1

        elif isPreto(origem):
            movePeca(origem,destino)
            jogador = 0
        

def jogadaPeca(origem,destino):
    global jogador
    rawDist = calcDist(origem,destino)
    distancia = len(diagonal)
    tileCaminho = acessaTile(origem, rawDist[0]//2, rawDist[1]//2)[0]

    if isVazio(destino):
        if distancia == 2:
            if isBranco(origem) and jogador == 0 and (rawDist == [-1,-1] or rawDist == [-1,1]):
                movePeca(origem, destino)
                jogador = 1

            elif isPreto(origem) and jogador == 1 and (rawDist == [1,-1] or rawDist == [1,1]):
                movePeca(origem, destino)
                jogador = 0
        
        elif distancia == 3: 
            #essa checagem está errada, não é possível pelas regras comer para trás como dama
            #acabei de perceber outro problema e como ele afeta a come mais
            #refatorar (ESSE É TRIVIAL)
            if isBranco(origem) and jogador == 0 and isPreto(tileCaminho):
                comePeca(origem, destino)
                if comeMais(destino):
                    jogador = 0
                else:
                    jogador = 1

            elif isPreto(origem) and jogador == 1 and isBranco(tileCaminho):
                comePeca(origem, destino)
                if comeMais(destino):
                    jogador = 1
                else:
                    jogador = 0
