Sudoku Solver – Streamlit Web App

This project is a Sudoku puzzle solver built using Python and Streamlit, developed as part of my software development internship at SkillCraft Technology.

It allows users to paste an unsolved Sudoku grid into a web interface and get the solved version instantly using the backtracking algorithm.

  Features

 Accepts a 9x9 Sudoku grid with empty cells as `0`
- Solves puzzles using a recursive backtracking algorithm
- Validates input and displays the solution interactively
-  Uses NumPy for efficient array operations
-  Built with Streamlit – deployable as a web app

 Sample Input Format

Paste 9 rows with 9 space-separated digits in the text area (use `0` for blanks):

5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9



 How to Run :-
pip install streamlit numpy
Run the app
python app.py
streamlit run app.py
The app will open in your browser. Paste your Sudoku puzzle and click "Solve Sudoku".

How It Works:-

-The app reads the 9x9 puzzle grid from user input.
-It uses a recursive backtracking algorithm to try valid numbers in empty cells.
-If the puzzle is solvable, it shows the completed board.
-If not, it returns an error message.




