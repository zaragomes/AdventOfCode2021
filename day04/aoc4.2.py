from day4 import get_numbers_and_boards, find_number_on_board, is_winning_board


def find_last_winning_board():
    called_numbers = []
    winning_boards_indexes = []
    numbers, boards = get_numbers_and_boards()
    marked_boards = [set() for _ in boards]

    for number in numbers:
        called_numbers.append(number)
        for index, (board, marked_board) in enumerate(zip(boards, marked_boards)):
            match = find_number_on_board(board, number)
            if match:
                marked_board.add(match)
            if is_winning_board(marked_board):
                if index not in winning_boards_indexes:
                    winning_boards_indexes.append(index)
                if len(winning_boards_indexes) == len(boards):
                    return board, called_numbers


def calculate_score(board, ticked_numbers):
    total_sum = 0
    for row in board:
        total_sum += (sum(i for i in row))
    for i in ticked_numbers:
        for row in board:
            if i in row:
                total_sum -= i

    return total_sum * ticked_numbers[-1]


winning_board, called_numbers = find_last_winning_board()
print("The winning board and called numbers are")
print(winning_board)
print(called_numbers)

print(calculate_score(winning_board, called_numbers))



