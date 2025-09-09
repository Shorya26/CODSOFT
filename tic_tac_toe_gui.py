import tkinter as tk
import math
from tkinter import messagebox

# ---------- Game Logic ----------
def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

def evaluate(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return 10 if row[0] == "X" else -10

    # Check cols
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return 10 if board[0][col] == "X" else -10

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return 10 if board[0][0] == "X" else -10

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return 10 if board[0][2] == "X" else -10

    return 0

def minimax(board, depth, is_max, alpha, beta):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = max(best, minimax(board, depth+1, False, alpha, beta))
                    board[i][j] = " "
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = min(best, minimax(board, depth+1, True, alpha, beta))
                    board[i][j] = " "
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = " "
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

# ---------- GUI ----------
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - AI")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text=" ", font=("Arial", 24), width=5, height=2,
                                command=lambda row=i, col=j: self.player_move(row, col))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def player_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = "O"
            self.buttons[row][col].config(text="O", state="disabled")

            if evaluate(self.board) == -10:
                messagebox.showinfo("Result", "🎉 You Win!")
                self.reset_game()
                return

            if not is_moves_left(self.board):
                messagebox.showinfo("Result", "It's a Draw!")
                self.reset_game()
                return

            # AI move
            ai_move = find_best_move(self.board)
            self.board[ai_move[0]][ai_move[1]] = "X"
            self.buttons[ai_move[0]][ai_move[1]].config(text="X", state="disabled")

            if evaluate(self.board) == 10:
                messagebox.showinfo("Result", "AI Wins! 💻")
                self.reset_game()
                return

            if not is_moves_left(self.board):
                messagebox.showinfo("Result", "It's a Draw!")
                self.reset_game()
                return

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ", state="normal")

# ---------- Run ----------
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

    # import tkinter as tk

    # root = tk.Tk()
    # root.title("Test Window")
    # root.geometry("200x100")
    # label = tk.Label(root, text="Tkinter works!")
    # label.pack()
    # root.mainloop()
