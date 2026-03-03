from pydamas.utils import extras as ex
from pydamas.commands import condicionais as cd

def constroi_linha(numero:str) -> list:
    linha = []
    for letra in ex.LETRAS:
        linha.append([letra + numero,0,0])

    return linha

def constroi_colunas() -> None:
    for numero in ex.NUMEROS:
        ex.tabuleiro.append(constroi_linha(numero))

def constroi_coordenadas() -> None:
    for letra in ex.LETRAS:
        for numero in ex.NUMEROS:
            ex.coordenadas.append(letra + numero)

def insere_tiles() -> None:
    for coordenada in ex.coordenadas:
        distancia = ex.calcula_distancia("A1",coordenada)
        
        if not cd.e_par(distancia[0] + distancia[1]):
            ex.acessa_tile(coordenada)[1] = ex.QUADRADO_PRETO
        
        if cd.e_quadrado_preto(coordenada):
            if distancia[0] < 3:
                ex.acessa_tile(coordenada)[2] = ex.PECA_PRETA
            elif distancia[0] > 4:
                ex.acessa_tile(coordenada)[2] = ex.PECA_BRANCA

def constroi_tabuleiro() -> None:
    constroi_coordenadas()
    constroi_colunas()
    insere_tiles()