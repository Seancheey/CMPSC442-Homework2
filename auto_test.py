"""
`$ python -O auto_test.py` to ignore assert statements
Change import id
"""
import qxs20 as my_main


# q1_1
assert my_main.num_placements_all(8) == 4426165368
assert my_main.num_placements_one_per_row(8) == 16777216


# q1_2
assert my_main.n_queens_valid([0, 2]) #True
assert my_main.n_queens_valid([0, 3, 1]) #True
assert my_main.n_queens_valid([5, 0, 4, 1]) #True
assert my_main.n_queens_valid([0,1]) == False #False
assert my_main.n_queens_valid([0,0]) == False #False
assert my_main.n_queens_valid([0, 2, 1]) == False #False
assert my_main.n_queens_valid([5, 0, 4, 3]) == False #False


# q1_3
# care order
solutions = my_main.n_queens_solutions(4)
assert next(solutions) == [1, 3, 0, 2]
assert next(solutions) == [2, 0, 3, 1]
assert list(my_main.n_queens_solutions(6)) == [[1, 3, 5, 0, 2, 4], [2, 5, 1, 4, 0, 3], [3, 0, 4, 1, 5, 2], [4, 2, 0, 5, 3, 1]]
assert len(list(my_main.n_queens_solutions(8))) == 92


# q2_1
b = [[True, False], [False, True]]
p = my_main.LightsOutPuzzle(b)
assert p.get_board() == [[True, False], [False, True]]
b = [[True, True], [True, True]]
p = my_main.LightsOutPuzzle(b)
assert p.get_board() == [[True, True], [True, True]]


# q2_2
p = my_main.create_puzzle(2, 2)
assert p.get_board() == [[False, False], [False, False]]
p = my_main.create_puzzle(2, 3)
assert p.get_board() == [[False, False, False], [False, False, False]]


# q2_3
p = my_main.create_puzzle(3, 3)
p.perform_move(1, 1)
assert p.get_board() == [[False, True, False], [True, True, True], [False, True, False]]
p = my_main.create_puzzle(3, 3)
p.perform_move(0, 0)
assert p.get_board() == [[True, True, False], [True, False, False], [False, False, False]]
p = my_main.create_puzzle(3, 3)
p.perform_move(1, 2)
assert p.get_board() == [[False, False, True], [False, True, True], [False, False, True]]


# q2_4
# xjb xie; sugget doing the check on x, y value in if random statement
p = my_main.create_puzzle(3, 3)
p.scramble()
# print p.get_board()
# assert p.get_board() != [[False, False, False], [False, False, False], [False, False, False]]


# q2_5
b = [[True, False], [False, True]]
p = my_main.LightsOutPuzzle(b)
assert p.is_solved() == False
b = [[False, False], [False, False]]
p = my_main.LightsOutPuzzle(b)
assert p.is_solved()


# q2_6
p = my_main.create_puzzle(3, 3)
p2 = p.copy()
assert p.get_board() == p2.get_board()
p = my_main.create_puzzle(3, 3)
p2 = p.copy()
p.perform_move(1, 1)
assert (p.get_board() == p2.get_board()) == False


# q2_7
p = my_main.create_puzzle(2, 2)
# for move, new_p in p.successors():
# 	print move, new_p.get_board()
assert map(lambda x: (x[0], x[1].get_board()), list(p.successors())) == [ \
((0, 0), [[True, True], [True, False]]), \
((0, 1), [[True, True], [False, True]]), \
((1, 0), [[True, False], [True, True]]), \
((1, 1), [[False, True], [True, True]])]

map_res = {2: 6, 3: 12, 4: 20, 5: 30}
for i in range(2, 6):
	p = my_main.create_puzzle(i, i + 1)
	assert len(list(p.successors())) == map_res[i]
	# print len(list(p.successors()))


# q2_8
p = my_main.create_puzzle(2, 3)
for row in range(2):
	for col in range(3):
		p.perform_move(row, col)
assert p.find_solution() == [(0, 0), (0, 2)]
b = [[False, False, False], [False, False, False]]
b[0][0] = True
p = my_main.LightsOutPuzzle(b)
assert p.find_solution() is None
p = my_main.create_puzzle(3, 3)
p.perform_move(1, 0)
p.perform_move(1, 1)
p.perform_move(1, 2)
assert p.find_solution() == [(1, 0), (1, 1), (1, 2)]


"""
# care diff function name call
# q3_1
p = my_main.LinkDisk(4, 2)
assert p.get_disk() == [1, 2, 0, 0]
# print map(lambda x: (x[0].get_disk(), x[1]), list(p.gen_next_move()))
assert map(lambda x: (x[0].get_disk(), x[1]), list(p.gen_next_move())) == [ \
([0, 2, 1, 0], (0, 2)), \
([1, 0, 2, 0], (1, 2)), \
]

p2 = p.copy()
assert p.get_disk() == p2.get_disk()

p.exec_move(0, 2)
assert (p.get_disk() == p2.get_disk()) == False

p = my_main.LinkDisk(4, 2)
p.exec_move(0, 2)
p.exec_move(1, 3)
assert p.is_identical_solved()
# better assert len equation
assert my_main._solve_disks_switch(4, 2, True) == [(0, 2), (1, 3)]
assert my_main.solve_identical_disks(4, 2) == [(0, 2), (1, 3)]
assert my_main.solve_identical_disks(4, 3) == [(1, 3), (0, 1)]
assert my_main.solve_identical_disks(5, 2) == [(0, 2), (1, 3), (2, 4)]
assert my_main.solve_identical_disks(5, 3) == [(1, 3), (0, 1), (2, 4), (1, 2)]


# q3_2
p = my_main.LinkDisk(4, 2)
p.exec_move(0, 2)
p.exec_move(2, 3)
p.exec_move(1, 2)
assert p.is_distinct_solved()
# better assert len equation
assert my_main._solve_disks_switch(4, 2, False) == [(0, 2), (2, 3), (1, 2)]
assert my_main.solve_distinct_disks(4, 2) == [(0, 2), (2, 3), (1, 2)]
assert my_main.solve_distinct_disks(5, 2) == [(0, 2), (1, 3), (2, 4)]

assert my_main.solve_distinct_disks(4, 3) == [(1, 3), (0, 1), (2, 0), (3, 2), (1, 3), (0, 1)]
assert my_main.solve_distinct_disks(5, 3) == [(1, 3), (2, 1), (0, 2), (2, 4), (1, 2)]
"""
