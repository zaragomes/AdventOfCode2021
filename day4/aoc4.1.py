from day4 import get_numbers_and_boards, find_number_on_board, is_winning_board

# numbers, boards = get_numbers_and_boards()
# find_number_on_board(boards[0], 4)
# print(numbers)
# print(boards)
# print(WINNING_COMBOS)


def find_winning_board():
    called_numbers = []
    numbers, boards = get_numbers_and_boards()
    marked_boards = [set() for _ in boards]
    # print(numbers)
    # print(boards)
    # print(marked_boards)
    for number in numbers:
        called_numbers.append(number)
        for board, marked_board in zip(boards, marked_boards):
            match = find_number_on_board(board, number)
            if match:
                marked_board.add(match)
            if is_winning_board(marked_board):
                return board, called_numbers


def calculate_score(board, called_numbers):
    total_sum = 0
    for row in board:
        total_sum += (sum(i for i in row))
    for i in called_numbers:
        if any(i in row for row in board):
            total_sum -= i

    return total_sum * called_numbers[-1]


winning_board, called_numbers = find_winning_board()
print(calculate_score(winning_board, called_numbers))



