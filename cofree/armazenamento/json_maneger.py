import json
from pathlib import Path


DIRETORIO_PROJETO = Path(__file__).resolve().parents[2]
DIRETORIO_DADOS = DIRETORIO_PROJETO / "data"
ARQUIVO_DADOS = DIRETORIO_DADOS / "dados.json"


DADOS_INICIAIS = {
    "cadastro_realizado": False,
    "saldo_inicial": None,
    "movimentacoes": [],
    "metas": [],
}


def carregar_dados():
    DIRETORIO_DADOS.mkdir(parents=True, exist_ok=True)

    if not ARQUIVO_DADOS.exists():
        salvar_dados(DADOS_INICIAIS.copy())

    with ARQUIVO_DADOS.open("r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados


def salvar_dados(dados):
    DIRETORIO_DADOS.mkdir(parents=True, exist_ok=True)

    with ARQUIVO_DADOS.open("w", encoding="utf-8") as arquivo:
        json.dump(
            dados,
            arquivo,
            indent=4,
            ensure_ascii=False,
        )


def verificar_cadastro():
    dados = carregar_dados()

    return dados["cadastro_realizado"]