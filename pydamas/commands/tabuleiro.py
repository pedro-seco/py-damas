from pydamas.commands import construtores as ct
from pydamas.commands import condicionais as cd

diagonais = [[],[],[],[]]

def acessa_tile(tile: str, i = 0, j = 0) -> str:
    index = retorna_index(tile)
    linha = index[0]
    coluna = index[1]

    return ct.tabuleiro[linha+i][coluna+j]


def calcula_distancia(ponto1:list, ponto2:list) -> list: 
    return [retorna_index(ponto2)[0] - retorna_index(ponto1)[0],
            retorna_index(ponto2)[1] - retorna_index(ponto1)[1]
            ]

def contas_pecas() -> list:
    pecasPretas = 0
    pecasBrancas = 0

    for linha in ct.tabuleiro:
        for coluna in ct.tabuleiro:
            if cd.e_peca_preta(coluna[2]):
                pecasPretas += 1

            if cd.e_peca_preta(coluna[2]):
                pecasBrancas += 1
    
    return [pecasBrancas, pecasPretas]

def cria_diagonais(tile:str) -> list[list]:
    global diagonais
    diagonais = [[],[],[],[]]

    for linha in range(8):
        for coluna in range(8):
            listaDist = calcula_distancia(tile, ct.tabuleiro[linha][coluna][0])
        
            if not cd.e_quadrado(listaDist):
                continue
            
            match cd.qual_direcao(listaDist):
                case 1: #Primeiro Quadrante
                    diagonais[0].append(ct.tabuleiro[linha][coluna][0])
                case 2: #Segundo Quadrante
                    diagonais[1].append(ct.tabuleiro[linha][coluna][0])
                case 3: #Terceiro Quadrante
                    diagonais[2].append(ct.tabuleiro[linha][coluna][0])
                case 4: #Quarto Quadrante
                    diagonais[3].append(ct.tabuleiro[linha][coluna][0])

    # As lista do primeiro e segundo quadrante precisam ser invertidas
    # para que elas fiquem na ordem Origem -> Destino
    diagonais[0].reverse()
    diagonais[1].reverse()
    return diagonais

def define_caminho(origem:str, destino:str) -> list:
    caminho = []
    cria_diagonais(origem)

    for diagonal in diagonais:
        if destino in diagonal:
            final = diagonal.index(destino)+1
            caminho = diagonal[:final]
            return caminho

def procura_promo() -> None:
        
    for coluna in range(8):
        if ct.tabuleiro[0][coluna][2] == "Peça Branca":
            ct.tabuleiro[0][coluna][2] = "Rainha Branca"

        if ct.tabuleiro[7][coluna][2] == "Peça Preta":
            ct.tabuleiro[7][coluna][2] = "Rainha Preta"


def retorna_index(tile:str) -> list:
    letras = "ABCDEFGH"
    coluna = letras.find(tile[0])
    linha = int(tile[1])-1

    return [linha,coluna]