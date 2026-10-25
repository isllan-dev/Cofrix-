import customtkinter as ctk


def mostrar_erro(app, titulo, mensagem):
    """Mostra uma janela de erro personalizada do Cofree."""

    janela = ctk.CTkToplevel(app)
    janela.title(titulo)
    janela.geometry("390x250")
    janela.resizable(False, False)
    janela.configure(fg_color="#071512")
    janela.transient(app)
    janela.grab_set()

    # Centraliza a janela em relação à janela principal.
    janela.update_idletasks()

    largura = 390
    altura = 250

    x = app.winfo_rootx() + (app.winfo_width() - largura) // 2
    y = app.winfo_rooty() + (app.winfo_height() - altura) // 2

    janela.geometry(f"{largura}x{altura}+{x}+{y}")

    # Cartão principal.
    cartao = ctk.CTkFrame(
        janela,
        fg_color="#0B211A",
        corner_radius=16,
        border_width=1,
        border_color="#174B3B",
    )
    cartao.pack(
        fill="both",
        expand=True,
        padx=16,
        pady=16,
    )

    # Ícone de erro.
    ctk.CTkLabel(
        cartao,
        text="!",
        font=("Segoe UI", 25, "bold"),
        text_color="#FF657A",
        fg_color="#321C24",
        corner_radius=30,
        width=48,
        height=48,
    ).pack(pady=(18, 10))

    # Título.
    ctk.CTkLabel(
        cartao,
        text=titulo,
        font=("Segoe UI", 19, "bold"),
        text_color="#42E8B5",
    ).pack(pady=(0, 8))

    # Mensagem.
    ctk.CTkLabel(
        cartao,
        text=mensagem,
        font=("Segoe UI", 12),
        text_color="#C5E8E3",
        wraplength=310,
        justify="center",
    ).pack(padx=20, pady=(0, 16))

    # Botão para fechar o aviso.
    ctk.CTkButton(
        cartao,
        text="Entendi",
        width=130,
        height=36,
        corner_radius=9,
        fg_color="#32C98D",
        hover_color="#42E8B5",
        text_color="#06110F",
        font=("Segoe UI", 12, "bold"),
        command=janela.destroy,
    ).pack(pady=(0, 16))

    janela.focus_force()