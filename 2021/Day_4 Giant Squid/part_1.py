with open("input.txt", "r") as f:
    numbers = [int(i) for  i in f.readline()[:-1].split(",")]
    raw_boards = f.readlines()

# raw boards are having '\n' as a element and at the of the next boards
# like: '7 9 2 1 64\n'
# A double nested List of all boards
# - Each board is element of num_boards
# - Each row is element of each board
# - as there are 3 boards in the example
# check_boards is same as num_boards, but having False as default, as True will set if number is marked
num_boards = []
check_boards = []
# Iterating over each line in raw_boards list
for line in raw_boards:
    # if line is a new line as there's a space of new line in b/w of 2 boards
    if line == "\n":
        # creating row list and check list, check is same as row, but store bools
        row = []
        check = []
    else:
        # if line is not a new line, then append integers in row list
        # line[:-1], -1 to remove '\n' from end, and .split() to split nos. and typecasting nos. to int
        # check is having same numbers of bool values, by default False
        row.append([int(n) for n in line[:-1].split()])
        check.append([False for _ in line[:-1].split()])

        # if row's length is 5, means a single row complete
        if len(row)==5:
            # appends row in num_boards list
            num_boards.append(row)
            check_boards.append(check)


def check_row(row):
    """Return True if all elements in row are True
    else return False"""
    return True if (len(set(row))==1) and (True in row) else False

def check_column(board):
    """return True if all elements in a column of a board are True
    else return False"""

    for row in range(5):
        c = 0
        for ind in range(5):
            if board[ind][row] == True:
                c += 1
        if c == 5:
            return True
    return False
    ...

def get_winner(nums, boards, checks):
    """Take numbers, boards, checks nested lists as parameters.
    Find winner and return the winner's board index & last number of nums
    """
    # Iterating over numbers, in the group of 5
    for i in range(0, len(nums), 5):
        for n in nums[i:i+6]:
            # Iterating over each board
            for board in range(len(boards)):
                # Iterating over each row
                for row in range(5):
                    # Iterating over each element
                    for ind in range(5):
                        
                        # if num in ind row is same as n, then set checks same row no to True
                        if boards[board][row][ind] == n:
                            checks[board][row][ind] = True

                        # if num in ind column is same as n, then set checks same column no to True
                        if boards[board][ind][row] == n:
                            checks[board][ind][row] = True

                        # if check row returns True means a board having all numbers marked in row
                        if check_row(checks[board][row]):
                            return board, n

                        # if check_column returns True means a board having all numbers marked in column
                        if check_column(checks[board]):
                            return board, n


def count_score(num_board, check_board, n):
    """Take winner's board and check board & last no. as parameters.
    Calculate the sum of all unmarked numbers
    return the total score by multiplying sum with last number
    """
    s = 0
    for row in range(5):
        for ind in range(5):
            if not check_board[row][ind]:
                s += num_board[row][ind]
    
    return s, n, s*n

win_board, num = get_winner(numbers, num_boards, check_boards)
print(f"{win_board=}, {num=}")

print(count_score(num_boards[win_board], check_boards[win_board], num))