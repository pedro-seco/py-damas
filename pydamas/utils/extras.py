LETRAS = "ABCDEFGH"
NUMEROS = "12345678"

JOGADOR_BRANCO = 0
JOGADOR_PRETO = 1

QUADRADO_BRANCO = 0
QUADRADO_PRETO = 1

LINHAS = 8
COLUNAS = 8

VAZIO = 0
PECA_BRANCA = 2
PECA_PRETA = 4

RAINHA_BRANCA = 6
RAINHA_PRETA = 8

PRIMEIRO_QUADRANTE = 1
SEGUNDO_QUADRANTE = 2
TERCEIRO_QUADRANTE = 3
QUARTO_QUADRANTE = 4

jogador_preto = ""
jogador_branco = ""
jogador_vez = 0

tabuleiro = []
diagonais = [[],[],[],[]]
coordenadas = []

PECAS_IMAGENS = ["    ",    # Quadrado Branco(0) + Vazio(0) = 0
                 "||||",    # Quadradro Preto(1) + Vazio(0) = 1
                 " ⛀ ",    # Quadrado Branco(0) + Peça Branca(2) = 2
                 "|⛀ |",   # Quadrado Preto(1) + Peça Branca(2) = 3
                 " ⛂ ",    # Quadrado Branco(0) + Peça Preta(4) = 4
                 "|⛂ |",   # Quadrado Preto(1) + Peça Branca(4) = 5
                 " ⛃ ",    # Quadrado Branco(0) + Rainha Branca(6) = 6
                 "|⛁ |",   # Quadrado Preto(1) + Rainha Branca(6) = 7
                 " ⛃ ",    # Quadrado Branco(0) + Rainha Preta(8) = 8
                 "|⛃ |"    # Quadrado Preto (1) + Rainha Preta(8) = 9
                ]

def acessa_tile(tile: str, i = 0, j = 0) -> str:
    index = retorna_index(tile)
    linha = index[0]
    coluna = index[1]

    return tabuleiro[linha+i][coluna+j]

def calcula_distancia(ponto1:list, ponto2:list) -> list[int,int]: 
    return [retorna_index(ponto2)[0] - retorna_index(ponto1)[0],
            retorna_index(ponto2)[1] - retorna_index(ponto1)[1]
            ]

def retorna_index(tile:str) -> list[int,int]:
    coluna = LETRAS.find(tile[0])
    linha = int(tile[1])-1

    return [linha,coluna]

def procura_promo() -> None:
    for coluna in range(COLUNAS):
        if tabuleiro[0][coluna][2] == PECA_BRANCA:
            tabuleiro[0][coluna][2] = "Rainha Branca"

        if tabuleiro[7][coluna][2] == PECA_PRETA:
            tabuleiro[7][coluna][2] = "Rainha Preta"


