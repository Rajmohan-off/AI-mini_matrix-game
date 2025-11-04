"""
AI Number Arrange Game (GUI Edition)
Author: Rajmohan P

A Tkinter-based number puzzle (9x9) enhanced with a simple AI solver.
Players can manually swap tiles or let the AI solve step by step.

AI Algorithm:
- Greedy position correction.
- Finds the first misplaced number and swaps it to its correct position.
"""

import tkinter as tk
import random
import time
import threading

ROWS, COLS = 9, 9
TOTAL = ROWS * COLS


class NumberArrangeAI:
    def __init__(self, master):
        self.master = master
        self.master.title("🤖 AI Number Arrange Game (9×9)")
        self.master.configure(bg="#111")

        self.tiles = []
        self.selected = []
        self.moves = 0
        self.is_solving = False

        self.board = self.make_shuffled_board()

        self.create_ui()
        self.render_board()

    # ----------------------- Board Functions ----------------------- #
    def make_solved_board(self):
        nums = list(range(1, TOTAL + 1))
        return [nums[i * COLS:(i + 1) * COLS] for i in range(ROWS)]

    def make_shuffled_board(self, moves=500):
        nums = list(range(1, TOTAL + 1))
        for _ in range(moves):
            i, j = random.randrange(TOTAL), random.randrange(TOTAL)
            nums[i], nums[j] = nums[j], nums[i]
        return [nums[i * COLS:(i + 1) * COLS] for i in range(ROWS)]

    def is_solved(self):
        expected = 1
        for r in range(ROWS):
            for c in range(COLS):
                if self.board[r][c] != expected:
                    return False
                expected += 1
        return True

    # ----------------------- UI ----------------------- #
    def create_ui(self):
        self.frame = tk.Frame(self.master, bg="#111")
        self.frame.pack(pady=20)

        # Create 9×9 grid of buttons
        for r in range(ROWS):
            row_buttons = []
            for c in range(COLS):
                btn = tk.Button(
                    self.frame,
                    text="",
                    width=4,
                    height=2,
                    font=("Consolas", 12, "bold"),
                    bg="#222",
                    fg="white",
                    relief="raised",
                    command=lambda r=r, c=c: self.select_tile(r, c)
                )
                btn.grid(row=r, column=c, padx=2, pady=2)
                row_buttons.append(btn)
            self.tiles.append(row_buttons)

        self.info_label = tk.Label(self.master, text="Moves: 0", fg="white", bg="#111", font=("Arial", 12))
        self.info_label.pack(pady=10)

        control_frame = tk.Frame(self.master, bg="#111")
        control_frame.pack()

        tk.Button(control_frame, text="🔁 Shuffle", command=self.reset_board, bg="#007acc", fg="white").grid(row=0, column=0, padx=10)
        tk.Button(control_frame, text="🧠 AI Solve", command=self.start_ai_solve, bg="#00b33c", fg="white").grid(row=0, column=1, padx=10)
        tk.Button(control_frame, text="❌ Quit", command=self.master.quit, bg="#cc0000", fg="white").grid(row=0, column=2, padx=10)

    def render_board(self):
        for r in range(ROWS):
            for c in range(COLS):
                num = self.board[r][c]
                btn = self.tiles[r][c]
                btn.config(text=str(num))
                if len(self.selected) == 1 and self.selected[0] == (r, c):
                    btn.config(bg="#ffaa00")
                else:
                    btn.config(bg="#222")

        self.info_label.config(text=f"Moves: {self.moves}")

    def select_tile(self, r, c):
        if self.is_solving:
            return

        if (r, c) in self.selected:
            self.selected.remove((r, c))
        else:
            self.selected.append((r, c))

        if len(self.selected) == 2:
            self.swap_selected()
            self.selected = []

        self.render_board()

    def swap_selected(self):
        (r1, c1), (r2, c2) = self.selected
        self.board[r1][c1], self.board[r2][c2] = self.board[r2][c2], self.board[r1][c1]
        self.moves += 1
        self.render_board()

        if self.is_solved():
            self.show_victory()

    def show_victory(self):
        victory = tk.Toplevel(self.master)
        victory.title("🎉 Solved!")
        victory.configure(bg="#111")
        tk.Label(victory, text=f"🎉 You solved it in {self.moves} moves!", fg="white", bg="#111", font=("Arial", 14, "bold")).pack(padx=20, pady=20)
        tk.Button(victory, text="OK", command=victory.destroy, bg="#00b33c", fg="white").pack(pady=10)

    def reset_board(self):
        if self.is_solving:
            return
        self.board = self.make_shuffled_board()
        self.moves = 0
        self.selected = []
        self.render_board()

    # ----------------------- AI Logic ----------------------- #
    def ai_solve_step(self):
        expected = 1
        for r in range(ROWS):
            for c in range(COLS):
                if self.board[r][c] != expected:
                    correct_r = (expected - 1) // COLS
                    correct_c = (expected - 1) % COLS
                    cur_val = self.board[r][c]

                    # find where the correct number currently is
                    cur_r, cur_c = self.find_position(expected)
                    self.board[r][c], self.board[cur_r][cur_c] = self.board[cur_r][cur_c], self.board[r][c]
                    return True
                expected += 1
        return False

    def find_position(self, value):
        for r in range(ROWS):
            for c in range(COLS):
                if self.board[r][c] == value:
                    return r, c
        return None

    def start_ai_solve(self):
        if self.is_solving:
            return
        self.is_solving = True
        threading.Thread(target=self.ai_solve_loop, daemon=True).start()

    def ai_solve_loop(self):
        while not self.is_solved():
            moved = self.ai_solve_step()
            if moved:
                self.moves += 1
                self.render_board()
            time.sleep(0.05)
        self.is_solving = False
        self.show_victory()


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberArrangeAI(root)
    root.mainloop()
