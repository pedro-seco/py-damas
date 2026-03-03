from pydamas.utils import extras as ex
from pydamas.commands import condicionais as cd

def inicio() -> None:
    print("> ")
    print("> Bem Vindo ao Jogo de Damas")
    print("> ")
    print("> 1 - Começar Partida")
    print("> 2 - Ver Regras")
    print("> 3 - Sair")
    print("> ")

def registra_jogadores() -> None:
    ex.jogador_branco = input("> Jogador Branco (⛀ ), insira o nome que deseja usar: ")
    ex.jogador_preto = input("> Jogador Preto (⛂ ), insira o nome que deseja usar: ")

def sua_vez(jogador:str) -> None:
    print("> ")
    print(f"> {jogador}, é a sua vez!")

def comecar() -> None:
    print("> ")
    print("> A partida vai começar, preparem-se!")

def adeus() -> None:
    print("> ")
    print("> Até a próxima!")

def vitoria(vencedor: str) -> None:
    print(f"> Fim de partida!, o vencedor é o {vencedor}!")
    print("> Alexa, toque Sweet Victory do David Glen!")

def colunas() -> None:
    print(">       A    B    C    D    E    F    G    H")

def imprime_linha(linha:int) -> None:
    linha_impressa = '>    |'
    for coluna in range(ex.COLUNAS):
        tile = ex.tabuleiro[linha][coluna][1]
        peca = ex.tabuleiro[linha][coluna][2]
        linha_impressa += ex.PECAS_IMAGENS[tile + peca] + "|"
    print(linha_impressa)


def imprime_tabuleiro() -> str:
    for linha in range(ex.LINHAS):
        if linha == 0:
            print("> ")
            colunas()
            print(">    ┌----┬┬┬┬┬┬----┬┬┬┬┬┬----┬┬┬┬┬┬----┬┬┬┬┬┐")
            imprime_linha(linha)
            print(">    ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┤") 
        
        elif linha % 2 == 0:
            imprime_linha(linha)
            print(">    ├┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┤")  

        elif linha == 7:
            imprime_linha(linha)
            print(">    └┴┴┴┴┴----┴┴┴┴┴┴----┴┴┴┴┴┴----┴┴┴┴┴┴----┘")
            colunas()
            print("> ")
        
        else:
            imprime_linha(linha)
            print(">    ├┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┼┴┴┴┴┼┬┬┬┬┤")  
        