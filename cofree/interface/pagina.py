import customtkinter as ctk
from decimal import Decimal, InvalidOperation

from cofree.armazenamento.json_maneger import carregar_dados
from cofree.financeiro.operacoes import (
    calcular_valor_guardado,
    calcular_valor_investimento,
    calcular_valor_livre,
)
from utils.cores import (
    BG,
    CARD,
    GREEN,
    TEXT,
    MUTED,
    BORDER,
)
from cofree.interface.cartoes import create_card, section_title


AZUL = "#72B7FF"
AMARELO = "#F4C76A"
FUNDO_BARRA = "#26332B"


def obter_distribuicao():
    """Carrega o saldo inicial e calcula a distribuição financeira."""
    dados_cofree = carregar_dados()
    saldo_inicial = dados_cofree.get("saldo_inicial")

    if saldo_inicial is None:
        return None

    try:
        saldo = Decimal(str(saldo_inicial))
    except (InvalidOperation, ValueError, TypeError):
        return None

    if not saldo.is_finite() or saldo < 0:
        return None

    return {
        "saldo": saldo,
        "guardado": calcular_valor_guardado(saldo),
        "livre": calcular_valor_livre(saldo),
        "investimento": calcular_valor_investimento(saldo),
    }


def _criar_barra_distribuicao(parent, nome, valor, percentual, cor):
    """Cria uma linha com nome, barra de progresso e valor monetário."""
    linha = ctk.CTkFrame(parent, fg_color="transparent")
    linha.pack(fill="x", padx=20, pady=8)

    ctk.CTkLabel(
        linha,
        text=nome,
        width=100,
        anchor="w",
        text_color=MUTED,
        font=("Segoe UI", 12),
    ).pack(side="left")

    barra = ctk.CTkProgressBar(
        linha,
        height=8,
        progress_color=cor,
        fg_color=FUNDO_BARRA,
    )
    barra.pack(side="left", fill="x", expand=True, padx=12)
    barra.set(float(percentual))

    ctk.CTkLabel(
        linha,
        text=f"R$ {valor:.2f}",
        width=105,
        anchor="e",
        text_color=TEXT,
        font=("Segoe UI", 12),
    ).pack(side="right")


def draw_dashboard(app, parent):
    """Desenha o painel com cartões, distribuição e ações rápidas."""
    distribuicao = obter_distribuicao()

    if distribuicao is None:
        ctk.CTkLabel(
            parent,
            text="Nenhum saldo inicial válido foi encontrado.",
            font=("Segoe UI", 14),
            text_color=MUTED,
        ).pack(anchor="w", padx=20, pady=30)
        return

    section_title(parent, "Resumo financeiro")

    # O contêiner externo usa pack; os cartões usam grid apenas dentro dele.
    cartoes = ctk.CTkFrame(parent, fg_color="transparent")
    cartoes.pack(fill="x", pady=(0, 4))
    cartoes.grid_columnconfigure((0, 1, 2), weight=1, uniform="cartoes")

    dados_cartoes = [
        ("SALDO TOTAL", distribuicao["saldo"], "Dinheiro organizado"),
        ("GUARDAR · 50%", distribuicao["guardado"], "Sua reserva"),
        ("INVESTIR · 20%", distribuicao["investimento"], "Pensando no futuro"),
    ]

    for coluna, (titulo, valor, descricao) in enumerate(dados_cartoes):
        create_card(
            cartoes,
            titulo,
            f"R$ {valor:.2f}",
            descricao,
        ).grid(
            row=0,
            column=coluna,
            sticky="nsew",
            padx=(0 if coluna == 0 else 7, 0 if coluna == 2 else 7),
        )

    painel_distribuicao = ctk.CTkFrame(
        parent,
        fg_color=CARD,
        corner_radius=15,
        border_width=1,
        border_color=BORDER,
    )
    painel_distribuicao.pack(fill="x", pady=18)

    ctk.CTkLabel(
        painel_distribuicao,
        text="DISTRIBUIÇÃO DO DINHEIRO",
        font=("Segoe UI", 12, "bold"),
        text_color=TEXT,
    ).pack(anchor="w", padx=20, pady=(18, 12))

    _criar_barra_distribuicao(
        painel_distribuicao,
        "Guardar",
        distribuicao["guardado"],
        0.50,
        GREEN,
    )

    _criar_barra_distribuicao(
        painel_distribuicao,
        "Investir",
        distribuicao["investimento"],
        0.20,
        AZUL,
    )

    _criar_barra_distribuicao(
        painel_distribuicao,
        "Livre",
        distribuicao["livre"],
        0.30,
        AMARELO,
    )

    acoes = ctk.CTkFrame(parent, fg_color="transparent")
    acoes.pack(fill="x", pady=(0, 8))
    acoes.grid_columnconfigure((0, 1, 2), weight=1, uniform="acoes")

    botoes = [
        ("＋  Registrar entrada", "Registrar entrada"),
        ("−  Registrar saída", "Registrar saída"),
        ("⇄  Transferir valores", "Transferir valores"),
    ]

    for coluna, (rotulo, acao) in enumerate(botoes):
        ctk.CTkButton(
            acoes,
            text=rotulo,
            height=43,
            corner_radius=10,
            fg_color="#19251D",
            hover_color="#263D2D",
            text_color=TEXT,
            command=lambda nome=acao: app.show_notice(nome),
        ).grid(
            row=0,
            column=coluna,
            sticky="ew",
            padx=(0 if coluna == 0 else 5, 0 if coluna == 2 else 5),
        )


def draw_movements(app, parent):
    """Desenha a página de movimentações."""
    section_title(parent, "Movimentações")

    ctk.CTkLabel(
        parent,
        text="Suas movimentações aparecerão aqui.",
        font=("Segoe UI", 13),
        text_color=MUTED,
    ).pack(anchor="w", padx=10, pady=15)


def draw_categories(app, parent):
    """Mostra a distribuição atual com barras de progresso."""
    distribuicao = obter_distribuicao()
    section_title(parent, "Distribuição do dinheiro")

    if distribuicao is None:
        ctk.CTkLabel(
            parent,
            text="Cadastre um saldo válido para visualizar a distribuição.",
            font=("Segoe UI", 13),
            text_color=MUTED,
        ).pack(anchor="w", padx=10, pady=15)
        return

    categorias = [
        (
            "Guardar",
            "50% do saldo inicial",
            distribuicao["guardado"],
            0.50,
            GREEN,
        ),
        (
            "Investir",
            "20% do saldo inicial",
            distribuicao["investimento"],
            0.20,
            AZUL,
        ),
        (
            "Livre",
            "30% do saldo inicial",
            distribuicao["livre"],
            0.30,
            AMARELO,
        ),
    ]

    for nome, subtitulo, valor, percentual, cor in categorias:
        cartao = ctk.CTkFrame(
            parent,
            fg_color=CARD,
            corner_radius=15,
            border_width=1,
            border_color=BORDER,
        )
        cartao.pack(fill="x", pady=8)

        ctk.CTkLabel(
            cartao,
            text=nome,
            font=("Segoe UI", 17, "bold"),
            text_color=TEXT,
        ).pack(anchor="w", padx=20, pady=(17, 3))

        ctk.CTkLabel(
            cartao,
            text=subtitulo,
            font=("Segoe UI", 11),
            text_color=MUTED,
        ).pack(anchor="w", padx=20)

        ctk.CTkLabel(
            cartao,
            text=f"R$ {valor:.2f}",
            font=("Segoe UI", 23, "bold"),
            text_color=cor,
        ).pack(anchor="w", padx=20, pady=8)

        barra = ctk.CTkProgressBar(
            cartao,
            progress_color=cor,
            fg_color=FUNDO_BARRA,
            height=8,
        )
        barra.pack(fill="x", padx=20, pady=(0, 18))
        barra.set(percentual)


def draw_goals(app, parent):
    """Desenha a página de metas financeiras."""
    section_title(parent, "Metas financeiras")

    ctk.CTkLabel(
        parent,
        text="Suas metas financeiras aparecerão aqui.",
        font=("Segoe UI", 13),
        text_color=MUTED,
    ).pack(anchor="w", padx=10, pady=15)