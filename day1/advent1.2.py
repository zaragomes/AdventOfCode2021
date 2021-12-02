num_increase = 0

with open('input.txt') as f:
    arr_input = [int(line.strip()) for line in f]
    for i in range(1, len(arr_input)-2):
        if (arr_input[i] + arr_input[i+1] + arr_input[i+2]) > (arr_input[i-1] + arr_input[i] + arr_input[i+1]):
            num_increase += 1

print("The number of increases is: ", num_increase)