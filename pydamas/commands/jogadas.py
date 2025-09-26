from pydamas.commands import condicionais as cd
from pydamas.commands import tabuleiro as tb
from pydamas.commands import mensagens as msg
from pydamas.commands import construtores as ct
from pydamas.utils import extras as ex

def define_jogada(origem:str, destino:str) -> bool:

    if cd.e_move_peca(origem, destino):
        move_peca(origem, destino)
        return False
        
    if cd.e_come_peca(origem, destino):
        come_peca(origem, destino)
        if cd.peca_come_mais(destino):
            return True
        return False

    if cd.e_move_rainha(origem,destino):
        move_peca(origem,destino)
        return False

    if cd.e_come_rainha(origem,destino):
        come_peca(origem,destino)
        if cd.rainha_come_mais(destino):
            return True
        return False
    
    return True

def move_peca(origem:str,destino:str) -> None:
    tb.acessa_tile(destino)[2] = tb.acessa_tile(origem)[2]
    tb.acessa_tile(origem)[2] = "Vazio"

def come_peca(origem:str,destino:str) -> None:
    caminho = tb.define_caminho(origem, destino)
    tb.acessa_tile(caminho[-2])[2] = "Vazio" 
    move_peca(origem,destino)

def setup_jogada(jogador:str, outro_jogador:int) -> None:
    msg.sua_vez(jogador)
    ct.imprime_tabuleiro()
    jogada = input("> Informe seu movimento. (Ex. C6,D5)")
    origem = jogada[:2]
    destino = jogada[3:]

    if not define_jogada(origem, destino):
        ex.jogador_vez = outro_jogador
    
    tb.procura_promo()