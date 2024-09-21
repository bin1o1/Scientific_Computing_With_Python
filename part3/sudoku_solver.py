'''A program that solves sudoku for you'''

class Board:
    def __init__(self, board):          #Board class takes a board argument which is basically the puzzle, passes it to the board attribute of this class
        self.board = board

    def __str__(self):      #prints the board
        board_str = ''
        for row in self.board:
            row_str = [str(i) if i else '*' for i in row]           #prints the number if there's a number and prints * if there's no number(0).
            board_str += ' '.join(row_str)
            board_str += '\n'
        return board_str

    def find_empty_cell(self):          #method to find an empty cell (cell with element 0)
        for row, contents in enumerate(self.board):         #enumerate assigns a number to each list in the board attribute. it returns an iterable object. Number assigned starts from 0
            try:
                col = contents.index(0)         #returns the index of of the first 0 element in the list, which is also the column of the 0 element.
                return row, col
            except ValueError:          #if there's no 0 in the list then there's a value error. In this case, the iteration is continued.
                pass
        return None         #returns None if there's no zero in the whole sudoku

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):         #checks if the guess is valid in row, column and square. if True for all, returns True. Else, False.
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        if (next_empty := self.find_empty_cell()) is None:          #if there's no empty cell in the whole sudoku, returns True
            return True
        for guess in range(1, 10):              #iterates over the numbers 1-9, checks if the number is valid for the empty cell and if it is valid,
                                                # assigns the number to that cell. Calls the solver until the sudoku is finished. if it can't be finished 
                                                # then assigns that cell a 0 again, and tries for other numbers.
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess
                if self.solver():
                    return True
                self.board[row][col] = 0
        return False

def solve_sudoku(board):
    gameboard = Board(board)
    print(f'Puzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is unsolvable.')
    return gameboard

puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]
solve_sudoku(puzzle)