
def inicio() -> None:
    print("> ")
    print("> Bem Vindo ao Jogo de Damas")
    print("> ")
    print("> 1 - Começar Partida")
    print("> 2 - Ver Regras")
    print("> 3 - Sair")
    print("> ")

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