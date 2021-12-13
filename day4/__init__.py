
WINNING_COMBOS = []

for x in range(5):
    WINNING_COMBOS.append({(x,y) for y in range(5)})

for y in range(5):
    WINNING_COMBOS.append({(x,y) for x in range(5)})


def get_lines_from_input():
    with open('input.txt') as file:
        return [line.strip() for line in file]


def get_numbers_and_boards():
    input_array = get_lines_from_input()
    numbers = None
    current_board = None
    boards = []
    for l in input_array:
        if numbers is None:
            numbers = [int(s) for s in l.split(",")]
            continue
        if not l:
            if current_board:
                boards.append(current_board)
            current_board = []
            continue
        current_board.append([int(s) for s in l.split( )])
    if current_board:
        boards.append(current_board)

    return numbers, boards


def find_number_on_board(board, number):
    for y, row in enumerate(board):
        try:
            x = row.index(number)
        except ValueError:
            continue
        else:
            return x, y


def is_winning_board(marked_board):
    if len(marked_board) < 5:
        return False
    return any(marked_board.issuperset(combo) for combo in WINNING_COMBOS)