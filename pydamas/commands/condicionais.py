
from pydamas.commands import tabuleiro as tb
from pydamas.utils import extras as ex

def e_jogador_branco() -> bool:
    if ex.jogador_vez == ex.JOGADOR_BRANCO:
        return True
    return False

def e_jogador_preto() -> bool:
    if ex.jogador_vez == ex.JOGADOR_PRETO:
        return True
    return False

def e_peca_branca(tile:str) -> bool:
    if tb.acessa_tile(tile)[2] == "Peça Branca" or tb.acessa_tile(tile)[2] == "Rainha Branca":
        return True
    return False

def e_peca_preta(tile:str) -> bool:
    if tb.acessa_tile(tile)[2] == "Peça Preta" or tb.acessa_tile(tile)[2] == "Rainha Preta":
        return True
    return False

def e_quadrado(lista:list) -> bool:
    if abs(lista[0]) == abs(lista[1]):
        return True
    return False

def e_rainha(tile:str) -> bool:
    if tb.acessa_tile(tile)[2] == "Rainha Branca" or tb.acessa_tile(tile)[2] == "Rainha Preta":
        return True
    return False

def e_vazio(tile:str) -> bool:
    if tb.acessa_tile(tile)[2] == "Vazio":
        return True
    return False

def e_come_peca(origem:str, destino:str) -> bool:
    distancia = tb.calcula_distancia(origem, destino)
    pecaCaminho = tb.acessa_tile(destino, distancia[1]//2, distancia[0]//2)[0]

    if e_jogador_branco() and e_peca_branca(origem) and e_peca_preta(pecaCaminho) and e_vazio(destino):
        return True
    
    if e_jogador_preto() and e_peca_preta(origem) and e_peca_branca(pecaCaminho) and e_vazio(destino):
        return True
        
    return False

def e_come_rainha(origem:str, destino:str) -> bool:
    caminho = tb.define_caminho(origem,destino)
    
    if not e_move_rainha(origem,caminho[:-2]):
        return False
    
    if e_vazio(destino):
        if e_jogador_branco() and e_peca_branca(origem) and e_peca_preta(caminho[:-1]):
            return True
        
        if e_jogador_preto() and e_peca_preta(origem) and e_peca_branca(caminho[:-1]):
            return True

    return False

def e_move_peca(origem:str, destino:str) -> bool:
    distancia = tb.calcula_distancia(origem, destino)

    if not e_vazio(destino):
        return False
    
    if e_jogador_branco() and e_peca_branca(origem) and (distancia == [-1,1] or distancia == [-1,-1]):
        return True
    
    if e_jogador_preto() and e_peca_preta(origem) and (distancia == [1,-1] or distancia == [1,1]):
        return True
    
    return False


def e_move_rainha(origem:str, destino:str) -> bool:
    caminho = tb.define_caminho(origem,destino)

    for tile in caminho:
        if not tb.acessa_tile(tile)[2] == "Vazio":
            return False
        
    return True

def peca_come_mais(tile:str) -> bool:
    tb.cria_diagonais(tile)
    for quadrante in tb.diagonais:
        if e_vazio(quadrante[1]):
            if e_jogador_branco() and e_peca_preta(quadrante[0]):
                return True
            
            if e_jogador_branco() and e_peca_branca(quadrante[0]):
                return True
            
    return False

def rainha_come_mais(tile:str) ->bool:
    tb.cria_diagonais(tile)
    for quadrante in tb.diagonais:
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
    
    if linha < 0 and coluna > 0:
        return ex.SEGUNDO_QUADRANTE
    
    if linha > 0 and coluna < 0:
        return ex.TERCEIRO_QUADRANTE
    
    if linha > 0 and coluna > 0:
        return ex.QUARTO_QUADRANTE
    
    else:
        return 0

def e_vencedor_branco() -> bool:
    pecas = tb.contas_pecas()

    if e_fim_partida() and pecas[ex.JOGADOR_PRETO] == 0:
        return True
    return False

def e_vencedor_preto() -> bool:
    pecas = tb.contas_pecas()

    if e_fim_partida() and pecas[ex.JOGADOR_BRANCO] == 0:
        return True
    return False

def e_fim_partida() -> bool:
     pecas = tb.contas_pecas()

     if pecas[ex.JOGADOR_BRANCO] == 0 or pecas[ex.JOGADOR_PRETO] == 0:
        return True
     
     return False

