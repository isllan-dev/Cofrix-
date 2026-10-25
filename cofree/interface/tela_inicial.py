import customtkinter as ctk

from utils.cores import BG, GREEN, TEXT, MUTED, BORDER


def draw_initial_screen(app):
    app.initial_screen = ctk.CTkFrame(
        app,
        fg_color=BG,
        corner_radius=0,
    )
    app.initial_screen.grid(
        row=0,
        column=0,
        columnspan=2,
        sticky="nsew",
    )
    app.initial_screen.grid_columnconfigure(0, weight=1)
    app.initial_screen.grid_rowconfigure(0, weight=1)

    content = ctk.CTkFrame(
        app.initial_screen,
        fg_color="transparent",
        width=480,
    )
    content.grid(row=0, column=0, padx=24, pady=24)
    content.grid_columnconfigure(0, weight=1)

    ctk.CTkLabel(
        content,
        text="◈  Cofree",
        font=("Segoe UI", 30, "bold"),
        text_color=GREEN,
    ).grid(row=0, column=0, pady=(0, 34))

    card = ctk.CTkFrame(
        content,
        fg_color="#17231A",
        corner_radius=18,
        border_width=1,
        border_color=BORDER,
    )
    card.grid(row=1, column=0, sticky="ew")
    card.grid_columnconfigure(0, weight=1)

    ctk.CTkLabel(
        card,
        text="Vamos organizar seu dinheiro?",
        font=("Segoe UI", 23, "bold"),
        text_color=TEXT,
        wraplength=390,
    ).grid(row=0, column=0, padx=30, pady=(30, 10))

    ctk.CTkLabel(
        card,
        text=(
            "Para começar, informe quanto dinheiro você tem disponível hoje.\n"
            "O Cofree usará esse valor como seu saldo inicial."
        ),
        font=("Segoe UI", 12),
        text_color=MUTED,
        justify="center",
        wraplength=390,
    ).grid(row=1, column=0, padx=30, pady=(0, 24))

    ctk.CTkLabel(
        card,
        text="SALDO INICIAL (R$)",
        font=("Segoe UI", 11, "bold"),
        text_color=TEXT,
    ).grid(row=2, column=0, sticky="w", padx=30, pady=(0, 8))

    app.initial_balance_entry = ctk.CTkEntry(
        card,
        placeholder_text="Ex.: 250,00",
        height=48,
        font=("Segoe UI", 16),
        corner_radius=10,
        border_color=BORDER,
        fg_color=BG,
        text_color=TEXT,
    )
    app.initial_balance_entry.grid(
        row=3,
        column=0,
        sticky="ew",
        padx=30,
    )

    ctk.CTkButton(
        card,
        text="Continuar",
        height=46,
        corner_radius=10,
        font=("Segoe UI", 13, "bold"),
        fg_color=GREEN,
        hover_color="#35BD70",
        text_color="#07130B",
        command=app.handle_initial_balance,
    ).grid(
        row=4,
        column=0,
        sticky="ew",
        padx=30,
        pady=(18, 30),
    )

    ctk.CTkLabel(
        content,
        text="Simulação financeira · Nenhuma conta bancária é conectada.",
        font=("Segoe UI", 10),
        text_color=MUTED,
    ).grid(row=2, column=0, pady=(18, 0))