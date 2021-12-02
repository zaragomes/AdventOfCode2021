with open('input.txt') as file:
    input_array = [(line.strip()) for line in file]
    forward_increase = 0
    depth_increase = 0
    aim = 0

    for i in range(0, len(input_array)):
        fields = input_array[i].split(" ")
        if fields[0] == "forward":
            forward_increase += int(fields[1])
            depth_increase += int(fields[1]) * aim
        if fields[0] == "down":
            aim += int(fields[1])
        if fields[0] == "up":
            aim -= int(fields[1])

print(forward_increase * depth_increase)



