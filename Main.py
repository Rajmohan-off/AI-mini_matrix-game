import random
import sys
import time

ROWS, COLS = 9, 9
TOTAL = ROWS * COLS


def make_solved_board():
    nums = list(range(1, TOTAL + 1))
    return [nums[i * COLS:(i + 1) * COLS] for i in range(ROWS)]


def make_shuffled_board(moves=2000):
    nums = list(range(1, TOTAL + 1))
    for _ in range(moves):
        i, j = random.randrange(TOTAL), random.randrange(TOTAL)
        nums[i], nums[j] = nums[j], nums[i]
    return [nums[i * COLS:(i + 1) * COLS] for i in range(ROWS)]


def display_board(board):
    width = len(str(TOTAL))
    sep = " | "
    print("\n" + "-" * ((width + len(sep)) * COLS + 1))
    for row in board:
        print(" | ".join(str(x).rjust(width) for x in row))
    print("-" * ((width + len(sep)) * COLS + 1) + "\n")


def is_solved(board):
    expected = 1
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] != expected:
                return False
            expected += 1
    return True


def swap_cells(board, r1, c1, r2, c2):
    board[r1][c1], board[r2][c2] = board[r2][c2], board[r1][c1]


def find_position(board, value):
    """Find the current (row, col) of a given value."""
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == value:
                return r, c
    return None


def ai_solve_step(board):
    """
    Greedy AI solver:
    - Find the first misplaced number.
    - Swap it with the number currently in its correct position.
    """
    expected = 1
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] != expected:
                correct_r = (expected - 1) // COLS
                correct_c = (expected - 1) % COLS
                # Find where the expected number currently is
                cur_r, cur_c = find_position(board, expected)
                swap_cells(board, r, c, cur_r, cur_c)
                return (r, c, cur_r, cur_c)
            expected += 1
    return None


def main():
    print("=== 🤖 AI Number Arrange Game (9×9) ===")
    print("Arrange numbers 1–81 in ascending order.")
    print("Commands: 'swap r1 c1 r2 c2' | 'ai' | 'show' | 'quit'\n")

    board = make_shuffled_board()
    moves = 0

    while True:
        display_board(board)
        print(f"Moves: {moves}")

        if is_solved(board):
            print("🎉 Solved in", moves, "moves!")
            break

        cmd = input("Enter command: ").strip().lower()

        if cmd == "quit":
            print("👋 Exiting game.")
            break

        elif cmd == "show":
            print("Solved layout:")
            display_board(make_solved_board())
            continue

        elif cmd.startswith("swap"):
            try:
                _, r1, c1, r2, c2 = cmd.split()
                r1, c1, r2, c2 = int(r1)-1, int(c1)-1, int(r2)-1, int(c2)-1
                swap_cells(board, r1, c1, r2, c2)
                moves += 1
            except Exception as e:
                print("Invalid swap command. Use: swap r1 c1 r2 c2")
            continue

        elif cmd == "ai":
            print("🤖 AI is solving step-by-step...")
            step = 0
            while not is_solved(board):
                ai_solve_step(board)
                step += 1
                moves += 1
                display_board(board)
                print(f"AI Move {step}")
                time.sleep(0.1)
            print("✅ AI finished sorting the matrix!")
            break

        else:
            print("Invalid command! Try 'swap', 'ai', 'show', or 'quit'.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame interrupted. Bye!")
        sys.exit(0)
