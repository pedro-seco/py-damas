from pydamas.commands import condicionais as cd
from pydamas.commands import construtores as ct
from pydamas.commands import jogadas as jd
from pydamas.commands import mensagens as msg
from pydamas.commands import regras as r
from pydamas.commands import tabuleiro as tb
from pydamas.utils import extras as ex

ct.faz_tabuleiro()
jd.define_jogada("C6","D5")
ex.jogador_vez = 1
ct.imprime_tabuleiro()
jd.define_jogada("F3","E4")
ex.jogador_vez = 0
ct.imprime_tabuleiro()
jd.define_jogada("D5","F3")
ex.jogador_vez = 1
ct.imprime_tabuleiro()