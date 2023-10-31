def print_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))

def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(grid, i, j, num):
                        grid[i][j] = num
                        if solve_sudoku(grid):
                            return True
                        grid[i][j] = 0
                return False
    return True

def sudoku_solver():
    print("Enter the Sudoku puzzle (use '0' for blank spaces):")
    puzzle = [list(map(int, input().split())) for _ in range(9)]

    print("\nSudoku Puzzle:")
    print_grid(puzzle)

    if solve_sudoku(puzzle):
        print("\nSolved Sudoku:")
        print_grid(puzzle)
    else:
        print("No solution exists.")

sudoku_solver()
