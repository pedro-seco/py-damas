from pydamas.commands import construtores as ct
from pydamas.commands import jogadas as jd
from pydamas.commands import regras as r
from pydamas.commands import mensagens as msg
from pydamas.commands import condicionais as cd
from pydamas.utils import extras as ex

def inicia_programa() -> None:
    msg.inicio()
    resposta = int(input("> Insira o número desejado para navegar pelo menu: "))

    match resposta:
        case 1:
            msg.comecar()
            ex.registra_jogadores()
    
        case 2:
            r.regras()
            input("Aperte Enter quando estiver pronto para Jogar.")
            ex.registra_jogadores()

        case 3:
            msg.adeus()

def controla_jogo():
    ct.faz_tabuleiro()

    while cd.e_fim_partida is not True:

        if cd.e_jogador_branco():
            jd.setup_jogada(ex.jogador_branco,ex.JOGADOR_PRETO)

        if cd.e_jogador_preto():
            jd.setup_jogada(ex.jogador_preto,ex.JOGADOR_BRANCO)
        
    if cd.e_vencedor_branco():
        msg.vitoria(ex.jogador_branco)
    
    if cd.e_jogador_preto():
        msg.vitoria(ex.jogador_preto)

def main():
    inicia_programa()

if __name__ == "__main__":
    main()