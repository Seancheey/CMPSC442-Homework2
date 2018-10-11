############################################################
# CMPSC 442: Homework 2
############################################################

student_name = "Qiyi Shan"

############################################################
# Imports
############################################################

from random import random
from collections import deque

# Include your imports here, if any are used.

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

    def successors(self,last_move=(0,-1)):
        for y in range(last_move[0],self.row_num):
            for x in range(self.col_num):
                if (y==last_move[0] and x > last_move[1]) or y>last_move[0]:
                    yield ((y,x),self.copy().perform_move(y,x))

    def find_solution(self):
        if self.is_solved():
            return []
        solve_queue = deque([([s[0]],s[1]) for s in self.successors()])
        while len(solve_queue) > 0:
            moves,puzzle = solve_queue.popleft()
            if puzzle.is_solved():
                return moves
            for successor in puzzle.successors(last_move=moves[-1]):
                solve_queue.append((moves+[successor[0]],successor[1]))

def create_puzzle(rows, cols):
    return LightsOutPuzzle([[False]*cols for _ in range(rows)])

############################################################
# Section 3: Linear Disk Movement
############################################################

class MoveSeries:
    __slots__ = "move","last_move"

    def __init__(self,move,last_move=None):
        self.move = move
        self.last_move = last_move

class DiskPuzzle(object):
    __slots__ = "distinct","board", "board_len", "disk_num"
    empty = -1
    NA = 10086

    def __init__(self, board, disk_num, distinct):
        self.distinct = distinct
        self.disk_num = disk_num
        self.board = board
        self.board_len = len(self.board)

    def copy(self):
        return DiskPuzzle(self.board[:],self.disk_num,self.distinct)

    def solved(self):
        for i in range(1,self.disk_num+1):
            if self.distinct:
                if self.board[-i] != i-1:
                    return False
            else:
                if self.board[-i] is DiskPuzzle.empty:
                    return False
        return True

    def move(self,start,end):
        self.board[start],self.board[end] = self.board[end],self.board[start]
        return self

    def successors(self,last_moves=None,iterated_board=None):
        if iterated_board is None:
            iterated_board = []
        for i,disk in enumerate(self.board):
            if disk == DiskPuzzle.empty:
                continue
            diffs = [2,1,-1,-2]
            for diff in diffs:
                if self.get(i+diff) == DiskPuzzle.empty and ((i+diff-1) == i or (self.get(i+diff-1) != DiskPuzzle.empty)):
                    new_puzzle = self.copy().move(i,i+diff)
                    if new_puzzle.board not in iterated_board:
                        yield (MoveSeries((i,i+diff),last_moves),new_puzzle)

    def get(self,pos):
        return self.board[pos] if pos < self.board_len and pos >= 0 else DiskPuzzle.NA

    def solve(self):
        if self.solved():
            return []
        queue = deque(list(self.successors()))
        iterated_board = []
        while len(queue) > 0:
            moves,puzzle = queue.popleft()
            if puzzle.solved():
                out = [moves.move]
                while moves.last_move is not None:
                    moves = moves.last_move
                    out.insert(0,moves.move)
                return out
            else:
                iterated_board.append(puzzle.board)
                for successor in puzzle.successors(last_moves=moves,iterated_board=iterated_board):
                    queue.append(successor)

def create_disk_puzzle(length, n, distinct):
    return DiskPuzzle([i if i < n else DiskPuzzle.empty for i in range(length)],n,distinct)

def solve_identical_disks(length, n):
    puzzle = create_disk_puzzle(length,n,False)
    return puzzle.solve()

def solve_distinct_disks(length, n):
    puzzle = create_disk_puzzle(length,n,True)
    return puzzle.solve()

def utest():
    print solve_distinct_disks(4,2)
    print solve_distinct_disks(5,2)
    print solve_distinct_disks(4,3)
    print solve_distinct_disks(5,5)

############################################################
# Section 4: Feedback
############################################################

feedback_question_1 = """
6 hours
"""

feedback_question_2 = """
I spent most of the time trying to decrease running time for LightsOutPuzzle.
eliminating repeat states are challenging.
There are many possible solutions to eliminate them but there are only a few efficent ones.
"""

feedback_question_3 = """
All of them. Especially LightOut.
"""
