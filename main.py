import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("400x500")

# Переменные
current_player = "X"
score = {"X": 0, "O": 0}
buttons = []

# Заголовок
title_label = tk.Label(window, text="Крестики-нолики", font=("Arial", 18))
title_label.pack(pady=10)

# Счёт
score_label = tk.Label(window, text=f"Счёт: X — {score['X']} | O — {score['O']}", font=("Arial", 14))
score_label.pack(pady=5)

# Фрейм для игрового поля
game_frame = tk.Frame(window)
game_frame.pack(expand=True)
