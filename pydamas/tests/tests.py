from pydamas.commands import condicionais as cd
from pydamas.commands import construtores as ct
from pydamas.commands import jogadas as jd
from pydamas.commands import impressao as im
from pydamas.commands import regras as r
from pydamas.utils import extras as ex

def test_imprime_tabuleiro_novo() -> None:
    ct.constroi_coordenadas()
    ct.constroi_colunas()
    ct.insere_tiles()
    im.imprime_tabuleiro()
