import customtkinter as ctk

from utils.cores import (
    BG,
    CARD,
    GREEN,
    TEXT,
    MUTED,
    BORDER,
)


def create_card(parent, title, value, description):
    card = ctk.CTkFrame(
        parent,
        fg_color=CARD,
        corner_radius=15,
        border_width=1,
        border_color=BORDER,
    )

    ctk.CTkLabel(
        card,
        text=title,
        font=("Segoe UI", 12),
        text_color=MUTED,
    ).pack(anchor="w", padx=18, pady=(18, 8))

    ctk.CTkLabel(
        card,
        text=value,
        font=("Segoe UI", 23, "bold"),
        text_color=TEXT,
    ).pack(anchor="w", padx=18)

    ctk.CTkLabel(
        card,
        text=description,
        font=("Segoe UI", 10),
        text_color=GREEN,
    ).pack(anchor="w", padx=18, pady=(8, 18))

    return card


def section_title(parent, title):
    ctk.CTkLabel(
        parent,
        text=title,
        font=("Segoe UI", 16, "bold"),
        text_color=TEXT,
    ).pack(anchor="w", pady=(0, 12))