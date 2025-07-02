import streamlit as st
import numpy as np

st.set_page_config(page_title="Sudoku Solver", layout="centered")
st.title("🧩 Sudoku Solver")

# --- Helper Functions ---
def is_valid(board, num, pos):
    row, col = pos

    # Row
    if num in board[row]:
        return False

    # Column
    if num in board[:, col]:
        return False

    # Box
    box_x = col // 3 * 3
    box_y = row // 3 * 3
    box = board[box_y:box_y + 3, box_x:box_x + 3]
    if num in box:
        return False

    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True

    row, col = empty
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False

def convert_to_array(input_grid):
    try:
        rows = input_grid.strip().split("\n")
        grid = [[int(num) for num in row.strip().split()] for row in rows]
        return np.array(grid)
    except:
        return None

# --- UI Input ---
st.markdown("Enter your **Sudoku puzzle** (use 0 for empty cells):")
example = "5 3 0 0 7 0 0 0 0\n6 0 0 1 9 5 0 0 0\n0 9 8 0 0 0 0 6 0\n8 0 0 0 6 0 0 0 3\n4 0 0 8 0 3 0 0 1\n7 0 0 0 2 0 0 0 6\n0 6 0 0 0 0 2 8 0\n0 0 0 4 1 9 0 0 5\n0 0 0 0 8 0 0 7 9"
puzzle_input = st.text_area("Paste 9 lines of numbers (space-separated):", value=example, height=200)

if st.button("Solve Sudoku"):
    grid = convert_to_array(puzzle_input)
    if grid is not None and grid.shape == (9, 9):
        original = grid.copy()
        if solve(grid):
            st.success("Sudoku Solved Successfully!")
            st.write("### Solution:")
            st.dataframe(grid.astype(int), use_container_width=True)
        else:
            st.error("No solution exists for the given puzzle.")
    else:
        st.error("Invalid input. Please enter a 9x9 grid with digits separated by spaces.")

