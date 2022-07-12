# build tic tac toe board w/ listcomp
board = [['_'] * 3 for i in range(3)]
print(board)
# set one space to X
board[1][2] = 'X'
print(board)
## UNPACK
# python sees this like this:
# board = []
# for i in range(3):
#     row = ['_'] * 3
#     board.append(row)

# now try the (wrong) shortcut - using '*' on a sequence
weird_board = [['_'] * 3] * 3
print(weird_board)
# now try to set one place
weird_board[1][2] = 'O'
print(weird_board)
## UNPACK
# python sees this like this:
# row = ['_'] * 3
# board = []
# for i in range(3):
#     board.append(row)
