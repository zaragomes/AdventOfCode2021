import urllib.request
import copy
import numpy as np


def get_mcb_of_pos(input_array, pos):
    mcb_number = 0
    np.sum(input_array, pos)
    if mcb_number >= 0:
        return 1
    else:
        return 0


with open('example.txt') as file:
    input_array = [list(line.strip()) for line in file]
    gamma_rate = ""
    epsilon_rate = ""
    num_one = [0 for i in range(0, len(input_array[0]))]

    width = len(input_array[0])
    og_array = input_array
    co2_array = input_array.copy()
    for pos in range(0, width):
        bit_one = get_mcb_of_pos(og_array, pos)

        for i in range(len(og_array)-1, -1, -1):
            if len(og_array) > 1:
                if int(og_array[i][pos]) != bit_one:
                    og_array.pop(i)
            else:
                break
    og_rate = int("".join(og_array[0]), 2)

    for pos in range(0, width):
        print(pos)
        bit_one = get_mcb_of_pos(co2_array, pos)
        print(bit_one)
        print(co2_array)
        for i in range(len(co2_array)-1, -1, -1):
            if len(co2_array) > 1:
                if int(co2_array[i][pos]) == bit_one:
                    print("popping array " + "".join(co2_array[i]) + " that matches this bit " + str(bit_one))
                    co2_array.pop(i)
                    print(co2_array)
            else:
                break

    co2_rate = int("".join(co2_array[0]), 2)


print(int(co2_rate) * int(og_rate))



