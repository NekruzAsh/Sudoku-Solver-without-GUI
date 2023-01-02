
def find_next_empty(puzzle):
#finds the next empty row, col in the puzzle not filled
#representing empty spaces with a -1
#return row, col (or (None, None) if there is none)

#using 0-8 for all of the index

    for r in range(9):
        for c in range(9):
            if puzzle [r][c]==-1:
                return r, c

    return None, None #if no spaces in the puzzle are empty


def is_valid(puzzle, col, row, guess):

    #checks whether the guess at that col/row in the puzzle is valid


#row:

    row_values=puzzle[row]
    if guess in row_values:
        return False

#columns:

    col_values=[puzzle[k][col] for k in range(9)]
    if guess in col_values:
        return False

    #iterate over 3 values in the row/col 

    row_start= (row//3) *3
    col_start= (col//3) *3

    for r in range(row_start, row_start, + 3):
        for c in range(col_start, col_start, +3):
            if puzzle[r][c] == guess:
                return False

    return True



def solve_sudoku(puzzle):
    #solving sudoku using the backtracking implementation
    # each inner lists inside of a list is the row in the puzzle

    row, col= find_next_empty(puzzle)

    if row is None:
        return True

    # if space available, input a number 1 - 9

    for guess in range(1,10):

        if is_valid(puzzle, col, row, guess):
            puzzle[row][col] = guess

            #now the puzzle value can be mutated until we reached the end of the program
            if solve_sudoku(puzzle):
                return True

        #if guess is not correct OR doesn't solve the puzzle, we need to backtrack!

        puzzle[row][col]=-1 #reseting the value at this row/col

        #if none of the guesses work, then the puzzle is unsolvable
        
    return False

if __name__ == '__main__':
    example=[
        [-1, -1, -1,   -1, 7, 4,   8, -1, -1],
        [-1, -1, -1,   -1, -1, 8,   7, 2, 6],
        [8, -1, -1,   -1, -1, -1,   3, -1, 5],

        [1, -1, 2,   -1, 8, -1,   4, -1, 9],
        [-1, -1, 8,   4, 3, -1,   1, 6, 2],
        [7, -1, -1,   -1, 1, 2,   5, -1, -1],

        [4, -1, -1,   8, 6, 5,   -1, -1, 3],
        [9, -1, 5,   -1, -1, 3,   -1, -1, -1],
        [-1, 8, 3,   -1, 9, -1,   2, 5, -1]]

    print(solve_sudoku(example))
    print(example)

        

