from pydamas.commands import construtores as ct
from pydamas.commands import jogadas as jd
from pydamas.commands import regras as re
from pydamas.commands import impressao as im
from pydamas.commands import condicionais as cd
from pydamas.utils import extras as ex

def inicia_programa() -> None:
    im.inicio()
    resposta = int(input("> Insira o número desejado para navegar pelo menu: "))

    match resposta:
        case 1:
            controla_jogo()
    
        case 2:
            re.regras()
            input("Aperte Enter quando estiver pronto para Jogar.")
            controla_jogo()

        case 3:
            im.adeus()
        

def controla_jogo() -> None:
    im.comecar()
    im.registra_jogadores()
    ct.constroi_tabuleiro()

    while cd.e_fim_partida is not True:

        if cd.e_jogador_branco():
            jd.setup_jogada(ex.jogador_branco,ex.JOGADOR_PRETO)

        if cd.e_jogador_preto():
            jd.setup_jogada(ex.jogador_preto,ex.JOGADOR_BRANCO)
        
    if cd.e_vencedor_branco():
        im.vitoria(ex.jogador_branco)
    
    if cd.e_jogador_preto():
        im.vitoria(ex.jogador_preto)

def main():
    inicia_programa()

if __name__ == "__main__":
    main()