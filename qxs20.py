############################################################
# CMPSC 442: Homework 2
############################################################

student_name = "Qiyi Shan"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.

def utest():
    print list(n_queens_solutions(4))
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

def possible_boards(n):
    board = [0] * n
    while board[0]!=n:
        yield board[:]
        board[-1] += 1
        for i in range(1,n):
            if board[-i] == n:
                board[-i],board[-i-1] = 0,board[-i-1]+1
            else:
                break

def n_queens_solutions(n):
    for board in possible_boards(n):
        if n_queens_valid(board):
            yield board


############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):
    __slots__ = "board"
    def __init__(self, board):
        self.board = board


    def get_board(self):
        return self.board

    def perform_move(self, row, col):
        pass

    def scramble(self):
        pass

    def is_solved(self):
        pass

    def copy(self):
        pass

    def successors(self):
        pass

    def find_solution(self):
        pass

def create_puzzle(rows, cols):
    pass

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
