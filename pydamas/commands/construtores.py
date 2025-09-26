from pydamas.utils import extras as ex

tabuleiro = []

def constroi_linha(numero:int, primeiro_tile:int, peca = "Vazio", primeira_peca = 0) -> list:
    tiles = ["Quadrado Branco", "Quadrado Preto"]
    pecas = ["Vazio", peca]
    linha = []

    for letra in range(8):
            if letra % 2 == 0:
                linha.append([ex.letras[letra] + numero,tiles[primeiro_tile],pecas[primeira_peca]])
            else:
                linha.append([ex.letras[letra] + numero,tiles[primeiro_tile-1],pecas[primeira_peca-1]])
    
    return linha

def constroi_linha2() -> list:
    for numero in ex.numeros:
        linha = []
        for letra in ex.letras:
            linha.append([letra + numero,[],[]])
        tabuleiro.append(linha)
    
    return tabuleiro


def faz_tabuleiro() -> list[list]:

    for num in ex.numeros:
        if ex.numeros.index(num) < 3:
            if ex.numeros.index(num) % 2 == 0:
                tabuleiro.append(constroi_linha(num,0,"Peça Preta",0))
            else:
                tabuleiro.append(constroi_linha(num,1,"Peça Preta",1))

        elif ex.numeros.index(num) >= 5:
            if ex.numeros.index(num) % 2 == 0:
                tabuleiro.append(constroi_linha(num,0,"Peça Branca",0))
            else:
                tabuleiro.append(constroi_linha(num,1,"Peça Branca",1))

        else:
            if ex.numeros.index(num) % 2 == 0:
                tabuleiro.append(constroi_linha(num,0))
            else:
                tabuleiro.append(constroi_linha(num,1))
                      
    return tabuleiro

def imprime_tabuleiro() -> str:
    linhas = []

    for coluna in range(8):
        for linha in range(8):
            codigo = 0
            linhas_prontas = []
            for item in ex.pecas_texto:
                if tabuleiro[coluna][linha][2] == item:
                    codigo += ex.pecas_texto.index(item)
            
            for item2 in ex.pecas_tiles:
                if tabuleiro[coluna][linha][1] == item2:
                    codigo += ex.pecas_tiles.index(item2)*10

            str_codigo = str(codigo)
            for chave in ex.pecas_imagens:
                if str_codigo == chave:
                    linhas.append(ex.pecas_imagens.get(str_codigo))

        linhas_prontas = "|".join(linhas)
        linhas = []

        if coluna == 0:
            print("> ")
            print(">       A    B    C    D    E    F    G    H")
            print(">    ┌----┬┬┬┬┬┬----┬┬┬┬┬┬----┬┬┬┬┬┬----┬┬┬┬┬┐")
            print("> ",coluna + 1,"  ","|", linhas_prontas,"|","  ", coluna + 1, sep="")
            print("> "," ","├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┤") 

        elif coluna == 7:
            print("> ",coluna + 1,"  ","|", linhas_prontas,"|","  ", coluna + 1, sep="")
            print(">    └┴┴┴┴┴----┴┴┴┴┴┴----┴┴┴┴┴┴----┴┴┴┴┴┴----┘")
            print(">       A    B    C    D    E    F    G    H")
            print("> ")

        elif coluna % 2 == 0:
            print("> ",coluna + 1,"  ","|", linhas_prontas,"|","  ", coluna + 1, sep="")
            print("> "," ","├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┤")     

        else:
            print("> ",coluna + 1,"  ","|", linhas_prontas,"|","  ", coluna + 1, sep="")
            print("> "," ","├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┤")    