############################################################
# CMPSC 442: Homework 2
############################################################

student_name = "Qiyi Shan"

############################################################
# Imports
############################################################

from random import random

# Include your imports here, if any are used.

def utest():
    p = create_puzzle(2, 2)
    p = create_puzzle(2, 3)
    for row in range(2):
        for col in range(3):
            p.perform_move(row, col)
    print p.find_solution()

############################################################
# Section 1: N-Queens
############################################################

def num_placements_all(n):
    def fact(num):
        return fact(num-1)*num if num > 1 else 1
    # nCr(n^2,n)
    return fact(n**2)/fact(n**2-n)/fact(n)

def num_placements_one_per_row(n):
    return n**n

def n_queens_valid(board):
    for x,y in enumerate(board):
        if y in board[:x] or y in board[x+1:]:
            return False
        for off in range(-len(board),len(board)):
            if off == 0 or x+off < 0 or x+off >= len(board):
                continue
            if board[x+off] in [y+off,y-off]:
                return False
    return True

def n_queens_helper(n,board):
    if len(board) == n:
        yield board
    else:
        for y in [yi for yi in range(n) if n_queens_valid(board+[yi])]:
            for ele in n_queens_helper(n,board+[y]):
                yield ele

def n_queens_solutions(n):
    for ele in n_queens_helper(n,[]):
        yield ele

############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):
    __slots__ = "board","row_num","col_num"

    def __init__(self, board):
        self.board = board
        self.row_num = len(self.board)
        self.col_num = len(self.board[0])

    def get_board(self):
        return self.board

    def perform_move(self, row, col):
        self.board[row][col] = not self.board[row][col]
        if row > 0:
            self.board[row-1][col] = not self.board[row-1][col]
        if row < self.row_num-1:
            self.board[row+1][col] = not self.board[row+1][col]
        if col > 0:
            self.board[row][col-1] = not self.board[row][col-1]
        if col < self.col_num-1:
            self.board[row][col+1] = not self.board[row][col+1]
        return self

    def scramble(self):
        for row in range(self.row_num):
            for col in range(self.col_num):
                 if random() < 0.5:
                     self.perform_move(row,col)

    def is_solved(self):
        for row in range(self.row_num):
            for col in range(self.col_num):
                if self.board[row][col] == True:
                    return False
        return True

    def copy(self):
        return LightsOutPuzzle([row[:] for row in self.board])

    def successors(self):
        for y in range(self.row_num):
            for x in range(self.col_num):
                yield ((y,x),self.copy().perform_move(y,x))

    def find_solution(self):
        if self.is_solved():
            return []
        solve_queue = [([s[0]],s[1]) for s in self.successors()]
        i = 0
        while i < len(solve_queue):
            moves,puzzle = solve_queue[i]
            if puzzle.is_solved():
                return moves
            last_move = moves[-1][1] + moves[-1][0]*self.col_num
            for successor in list(puzzle.successors())[last_move+1:]:
                    solve_queue.append((moves+[successor[0]],successor[1]))
            i+=1

def create_puzzle(rows, cols):
    return LightsOutPuzzle([[False]*cols for _ in range(rows)])

############################################################
# Section 3: Linear Disk Movement
############################################################

def solve_identical_disks(length, n):
    pass

def solve_distinct_disks(length, n):
    pass

############################################################
# Section 4: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

if __name__ == "__main__":
    utest()
