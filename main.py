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


# Метка текущего игрока
status_label = tk.Label(window, text=f"Ходит: {current_player}", font=("Arial", 14))
status_label.pack(pady=5)

def on_click(row, col):
    global current_player
    btn = buttons[row][col]
    if btn["text"] == "":
        btn["text"] = current_player
        if check_winner(current_player):
            score[current_player] += 1
            update_score()
            if score[current_player] == 3:
                messagebox.showinfo("Победа!", f"Игрок {current_player} выиграл серию!")
                reset_game(hard=True)
            else:
                messagebox.showinfo("Победа!", f"Игрок {current_player} выиграл раунд.")
                reset_game(hard=False)
        elif is_full():
            messagebox.showinfo("Ничья", "Ничья в этом раунде!")
            reset_game(hard=False)
        else:
            current_player = "O" if current_player == "X" else "X"
            status_label.config(text=f"Ходит: {current_player}")

def check_winner(player):
    for i in range(3):
        if all(buttons[i][j]["text"] == player for j in range(3)): return True
        if all(buttons[j][i]["text"] == player for j in range(3)): return True
    if all(buttons[i][i]["text"] == player for i in range(3)): return True
    if all(buttons[i][2 - i]["text"] == player for i in range(3)): return True
    return False

def is_full():
    return all(btn["text"] != "" for row in buttons for btn in row)

def update_score():
    score_label.config(text=f"Счёт: X — {score['X']} | O — {score['O']}")

def reset_game(hard=False):
    global current_player
    for row in buttons:
        for btn in row:
            btn["text"] = ""
    # Смена стартового игрока
    current_player = "O" if current_player == "X" else "X"
    status_label.config(text=f"Ходит: {current_player}")
    if hard:
        score["X"] = 0
        score["O"] = 0
        update_score()

# Создание кнопок
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(game_frame, text="", font=("Arial", 20), width=5, height=2,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

# Кнопка новой игры
reset_btn = tk.Button(window, text="Новая игра", font=("Arial", 12), command=lambda: reset_game(hard=True))
reset_btn.pack(pady=10)

window.mainloop()
