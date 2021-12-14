import urllib.request

with open('input.txt') as file:
    input_array = [list(line.strip()) for line in file]
    gamma_rate = ""
    epsilon_rate = ""
    num_one = [0 for i in range(0, len(input_array[0]))]

    for i in range(0, len(input_array)):
        for j in range(0, len(input_array[i])):
            if int(input_array[i][j]) == 1:
                num_one[j] += 1
            else:
                num_one[j] -= 1

    for j in range(0, len(input_array[0])):
        if int(num_one[j]) >= 1:
            gamma_rate = gamma_rate + "1"
            epsilon_rate = epsilon_rate + "0"
        else:
            gamma_rate = gamma_rate + "0"
            epsilon_rate = epsilon_rate + "1"

gamma_decimal = int(gamma_rate, 2)
epsilon_decimal = int(epsilon_rate, 2)

print(gamma_decimal * epsilon_decimal)



