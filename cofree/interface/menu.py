import customtkinter as ctk

from versao import VERSAO

from utils.cores import (
    SIDEBAR,
    CARD,
    GREEN,
    MUTED,
)


def build_sidebar(app):
    ctk.CTkLabel(
        app.sidebar,
        text="◈  cofree",
        font=("Segoe UI", 27, "bold"),
        text_color=GREEN,
    ).pack(anchor="w", padx=23, pady=(30, 35))

    ctk.CTkLabel(
        app.sidebar,
        text="MENU PRINCIPAL",
        font=("Segoe UI", 10, "bold"),
        text_color=MUTED,
    ).pack(anchor="w", padx=23, pady=(0, 12))

    app.nav_buttons = {}

    pages = [
        ("Painel", "▦"),
        ("Movimentações", "↕"),
        ("Categorias", "◫"),
        ("Metas", "◎"),
    ]

    for page, icon in pages:
        button = ctk.CTkButton(
            app.sidebar,
            text=f"  {icon}    {page}",
            anchor="w",
            height=44,
            corner_radius=10,
            fg_color="transparent",
            hover_color=CARD,
            text_color=MUTED,
            font=("Segoe UI", 13),
            command=lambda p=page: app.show_page(p),
        )

        button.pack(fill="x", padx=13, pady=4)
        app.nav_buttons[page] = button

    ctk.CTkLabel(
        app.sidebar,
        text="Suas finanças,\nsob seu controle.",
        font=("Segoe UI", 12),
        text_color=MUTED,
        justify="left",
    ).pack(side="bottom", anchor="w", padx=23, pady=(0, 8))

    ctk.CTkLabel(
        app.sidebar,
        text=f"Cofree • v{VERSAO}",
        font=("Segoe UI", 10),
        text_color=MUTED,
    ).pack(side="bottom", anchor="w", padx=23, pady=(0, 20))