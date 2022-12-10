import math


def isRowValid(board, row):
    r = [board[row][i] for i in range(9) if board[row][i].isdigit()]
    return len(set(r)) == len(r)


def isColumnValid(board, col):
    x = [var[col] for var in board if var[col].isdigit()]
    return len(set(x)) == len(x)


def isCellValid(board, row, col):
    var = board[row][col: col+3]
    var.extend(board[row+1][col: col+3])
    var.extend(board[row+2][col: col+3])
    var = [val for val in var if val.isdigit()]
    return len(set(var)) == len(var)


def isValidSudoku(board) -> bool:
    for i in range(len(board)):
        if not isRowValid(board, i):
            return False
        if not isColumnValid(board, i):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not isCellValid(board, i, j):
                return False
    return True


def isValid(s: str) -> bool:
    #storing matches
    dics = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }
    stack = []
    for x in s:
        # if no element in stack, add it to there
        if len(stack) == 0:
            stack.append(x)
        else:
            #if there IS element, pop element to match
            pt = stack.pop()
            #check if pt is OPENING parentheses
            if pt in dics:
                #if it match, move forward
                if x == dics[pt]:
                    continue
                else:
                    #append them back to stack
                    stack.append(pt)
                    stack.append(x)
            else:
                return False
    #if after deletion there is still elements, then it is          not valid
    if len(stack) == 0:
        return True
    else:
        return False

def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

def testsquare():
    num = 7
    assert 7*7 == 49

def testvalid():
    s = "()"
    assert isValid(s)
    assert isValid("(){}[]")
    assert isValid("({})")

def testsodokuT():
    board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    assert isValidSudoku(board)


def testsodokuF():
    board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    assert isValidSudoku(board)

def testequality():
    assert 10 == 11