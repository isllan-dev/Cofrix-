import customtkinter as ctk

from cofree.financeiro.validacoes import validar_saldo_inicial
from cofree.armazenamento.json_maneger import (
    salvar_dados,
    carregar_dados,
)
from cofree.interface.aviso import mostrar_erro

from utils.cores import (
    BG,
    SIDEBAR,
    TEXT,
    MUTED,
    GREEN,
    GREEN_DARK,
)

from cofree.interface.pagina import (
    draw_dashboard,
    draw_movements,
    draw_categories,
    draw_goals,
)

from cofree.interface.menu import build_sidebar
from cofree.interface.tela_inicial import draw_initial_screen


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class CofreeApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cofree | Controle financeiro")
        self.geometry("1100x700")
        self.minsize(900, 600)
        self.configure(fg_color=BG)

        self.current_page = None

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0,
            fg_color=SIDEBAR,
        )
        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew",
        )
        self.sidebar.grid_propagate(False)

        self.main = ctk.CTkFrame(
            self,
            fg_color=BG,
            corner_radius=0,
        )
        self.main.grid(
            row=0,
            column=1,
            sticky="nsew",
        )
        self.main.grid_columnconfigure(0, weight=1)
        self.main.grid_rowconfigure(1, weight=1)

        self.header = ctk.CTkFrame(
            self.main,
            fg_color=BG,
        )
        self.header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=30,
            pady=(25, 15),
        )

        self.content = ctk.CTkFrame(
            self.main,
            fg_color=BG,
            corner_radius=0,
        )
        self.content.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=30,
            pady=(0, 25),
        )
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_rowconfigure(0, weight=1)

        build_sidebar(self)

        # Verifica se o cadastro já foi realizado.
        dados_cofree = carregar_dados()

        cadastro_realizado = (
            dados_cofree.get("cadastro_realizado", False)
        )
        saldo_inicial = dados_cofree.get("saldo_inicial")

        if cadastro_realizado and saldo_inicial is not None:
            self.show_page("Painel")
        else:
            draw_initial_screen(self)

    def handle_initial_balance(self):
        """Valida e salva o saldo inicial informado pelo usuário."""
        valor_informado = self.initial_balance_entry.get()

        saldo_validado = validar_saldo_inicial(valor_informado)

        if saldo_validado is None:
            mostrar_erro(
                self,
                "Saldo inválido",
                "Digite um valor válido e não negativo.",
            )
            return

        dados_cofree = carregar_dados()
        dados_cofree["saldo_inicial"] = str(saldo_validado)
        dados_cofree["cadastro_realizado"] = True

        salvar_dados(dados_cofree)

        # Remove a tela inicial antes de exibir o painel.
        self.initial_screen.destroy()

        self.current_page = None
        self.show_page("Painel")

    def show_page(self, page):
        if page == self.current_page:
            return

        page_drawers = {
            "Painel": draw_dashboard,
            "Movimentações": draw_movements,
            "Categorias": draw_categories,
            "Metas": draw_goals,
        }

        if page not in page_drawers:
            raise ValueError(f"Página desconhecida: {page}")

        self.current_page = page

        for name, button in self.nav_buttons.items():
            if name == page:
                button.configure(
                    fg_color=GREEN_DARK,
                    text_color=GREEN,
                    font=("Segoe UI", 13, "bold"),
                )
            else:
                button.configure(
                    fg_color="transparent",
                    text_color=MUTED,
                    font=("Segoe UI", 13),
                )

        for widget in self.header.winfo_children():
            widget.destroy()

        titles = {
            "Painel": (
                "Visão geral",
                "Resumo da sua vida financeira.",
            ),
            "Movimentações": (
                "Movimentações",
                "Acompanhe suas entradas e saídas.",
            ),
            "Categorias": (
                "Categorias",
                "Veja como seu dinheiro está dividido.",
            ),
            "Metas": (
                "Metas financeiras",
                "Planeje suas próximas conquistas.",
            ),
        }

        title, subtitle = titles[page]

        ctk.CTkLabel(
            self.header,
            text=title,
            font=("Segoe UI", 28, "bold"),
            text_color=TEXT,
        ).pack(anchor="w")

        ctk.CTkLabel(
            self.header,
            text=subtitle,
            font=("Segoe UI", 12),
            text_color=MUTED,
        ).pack(anchor="w", pady=(5, 0))

        for widget in self.content.winfo_children():
            widget.destroy()

        page_frame = ctk.CTkScrollableFrame(
            self.content,
            fg_color=BG,
            corner_radius=0,
            scrollbar_button_color=GREEN_DARK,
            scrollbar_button_hover_color=GREEN,
        )

        page_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

        page_frame.grid_columnconfigure(0, weight=1)

        page_drawers[page](self, page_frame)

    def show_notice(self, action):
        dialog = ctk.CTkToplevel(self)
        dialog.title(action)
        dialog.geometry("330x155")
        dialog.configure(fg_color="#17231A")
        dialog.transient(self)
        dialog.grab_set()

        ctk.CTkLabel(
            dialog,
            text="Protótipo visual",
            font=("Segoe UI", 18, "bold"),
            text_color=TEXT,
        ).pack(pady=(24, 8))

        ctk.CTkLabel(
            dialog,
            text=(
                "Esta ação ainda não está ligada\n"
                "à lógica financeira."
            ),
            font=("Segoe UI", 12),
            text_color=MUTED,
            justify="center",
        ).pack()

        ctk.CTkButton(
            dialog,
            text="Entendi",
            fg_color=GREEN,
            hover_color="#35BD70",
            text_color="#07130B",
            command=dialog.destroy,
        ).pack(pady=10)