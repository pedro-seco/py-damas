from pydamas.utils import extras as ex

def e_jogador_branco() -> bool:
    if ex.jogador_vez == ex.JOGADOR_BRANCO:
        return True
    return False

def e_jogador_preto() -> bool:
    if ex.jogador_vez == ex.JOGADOR_PRETO:
        return True
    return False

def e_quadrado_branco(tile:str) -> bool:
    if ex.acessa_tile(tile)[1] == ex.QUADRADO_BRANCO:
        return True
    return False

def e_quadrado_preto(tile:str) -> bool:
    if ex.acessa_tile(tile)[1] == ex.QUADRADO_PRETO:
        return True
    return False


def e_peca_branca(tile:str) -> bool:
    if ex.acessa_tile(tile)[2] == ex.PECA_BRANCA or ex.acessa_tile(tile)[2] == ex.RAINHA_BRANCA:
        return True
    return False

def e_peca_preta(tile:str) -> bool:
    if ex.acessa_tile(tile)[2] == ex.PECA_PRETA or ex.acessa_tile(tile)[2] == ex.RAINHA_PRETA:
        return True
    return False

def e_quadrado(lista:list) -> bool:
    if abs(lista[0]) == abs(lista[1]):
        return True
    return False

def e_rainha(tile:str) -> bool:
    if ex.acessa_tile(tile)[2] == ex.RAINHA_BRANCA or ex.acessa_tile(tile)[2] == ex.RAINHA_PRETA:
        return True
    return False

def e_vazio(tile:str) -> bool:
    if ex.acessa_tile(tile)[2] == ex.VAZIO:
        return True
    return False

def e_come_peca(origem:str, destino:str) -> bool:
    distancia = ex.calcula_distancia(origem, destino)
    pecaCaminho = ex.acessa_tile(destino, distancia[1]//2, distancia[0]//2)[0]

    if e_jogador_branco() and e_peca_branca(origem) and e_peca_preta(pecaCaminho) and e_vazio(destino):
        return True
    
    if e_jogador_preto() and e_peca_preta(origem) and e_peca_branca(pecaCaminho) and e_vazio(destino):
        return True
        
    return False

def e_come_rainha(origem:str, destino:str) -> bool:
    caminho = define_caminho(origem,destino)
    
    if caminho is None:
        return False

    if not e_move_rainha(origem,caminho[:-2]):
        return False
    
    if e_vazio(destino):
        if e_jogador_branco() and e_peca_branca(origem) and e_peca_preta(caminho[:-1]):
            return True
        
        if e_jogador_preto() and e_peca_preta(origem) and e_peca_branca(caminho[:-1]):
            return True

    return False

def e_move_peca(origem:str, destino:str) -> bool:
    distancia = ex.calcula_distancia(origem, destino)

    if not e_vazio(destino):
        return False
    
    if e_jogador_branco() and e_peca_branca(origem) and (distancia == [-1,1] or distancia == [-1,-1]):
        return True
    

    if e_jogador_preto() and e_peca_preta(origem) and (distancia == [1,-1] or distancia == [1,1]):
        return True
    
    return False


def e_move_rainha(origem:str, destino:str) -> bool:
    caminho = define_caminho(origem,destino)
    
    if caminho is None:
        return False
    
    for tile in caminho:
        if not e_vazio(tile):
            return False
        
    return True

def peca_come_mais(tile:str) -> bool:
    define_diagonais(tile)
    for quadrante in ex.diagonais:
        if e_vazio(quadrante[1]):
            if e_jogador_branco() and e_peca_preta(quadrante[0]):
                return True
            
            if e_jogador_branco() and e_peca_branca(quadrante[0]):
                return True
            
    return False

def rainha_come_mais(tile:str) -> bool:
    define_diagonais(tile)
    for quadrante in ex.diagonais:
        if e_move_rainha(quadrante[0],quadrante[-3]) and e_vazio(quadrante[-1]):
            if e_jogador_branco() and e_peca_branca(tile) and e_peca_preta(quadrante[-2]):
                return True
            if e_jogador_branco() and e_peca_preta(tile) and e_peca_branca(quadrante[-2]):
                return True
        return False

def qual_direcao(lista:list) -> int:
    linha = lista[0]
    coluna = lista[1]

    if linha < 0 and coluna < 0:
        return ex.PRIMEIRO_QUADRANTE
    
    elif linha < 0 and coluna > 0:
        return ex.SEGUNDO_QUADRANTE
    
    elif linha > 0 and coluna < 0:
        return ex.TERCEIRO_QUADRANTE
    
    elif linha > 0 and coluna > 0:
        return ex.QUARTO_QUADRANTE
    
    else:
        return 0
    
def contas_pecas() -> list:
    pecasPretas = 0
    pecasBrancas = 0

    for coordenada in ex.coordenadas:
            if e_peca_branca(coordenada):
                pecasPretas += 1

            if e_peca_preta(coordenada):
                pecasBrancas += 1
    
    return [pecasBrancas, pecasPretas]

def e_vencedor_branco() -> bool:
    pecas = contas_pecas()

    if e_fim_partida() and pecas[ex.JOGADOR_PRETO] == 0:
        return True
    return False


def e_vencedor_preto() -> bool:
    pecas = contas_pecas()

    if e_fim_partida() and pecas[ex.JOGADOR_BRANCO] == 0:
        return True
    return False

def e_fim_partida() -> bool:
     pecas = contas_pecas()

     if pecas[ex.JOGADOR_BRANCO] == 0 or pecas[ex.JOGADOR_PRETO] == 0:
        return True
     return False

def e_par(numero:int) -> bool:
    if numero % 2 == 0:
        return True
    return False

def define_diagonais(coordenada:str) -> list[list]:
    ex.diagonais = [[],[],[],[]]

    for linha in range(ex.LINHAS):
        for coluna in range(ex.COLUNAS):
            listaDist = ex.calcula_distancia(coordenada, ex.tabuleiro[linha][coluna][0])
        
            if not e_quadrado(listaDist):
                continue
            
            match qual_direcao(listaDist):
                case ex.PRIMEIRO_QUADRANTE:
                    ex.diagonais[0].append(ex.tabuleiro[linha][coluna][0])
                case ex.SEGUNDO_QUADRANTE: 
                    ex.diagonais[1].append(ex.tabuleiro[linha][coluna][0])
                case ex.TERCEIRO_QUADRANTE:
                    ex.diagonais[2].append(ex.tabuleiro[linha][coluna][0])
                case ex.QUARTO_QUADRANTE:
                    ex.diagonais[3].append(ex.tabuleiro[linha][coluna][0])

    # As lista do primeiro e segundo quadrante precisam ser invertidas
    # para que elas fiquem na ordem Origem -> Destino
    ex.diagonais[0].reverse()
    ex.diagonais[1].reverse()
    return ex.diagonais

def define_caminho(origem:str, destino:str) -> list:
    caminho = []
    define_diagonais(origem)

    for diagonal in ex.diagonais:
        if destino in diagonal:
            final = diagonal.index(destino)+1
            caminho = diagonal[:final]
            return caminho