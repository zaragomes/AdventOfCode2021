import urllib.request

with open('input.txt') as file:
    input_array = [(line.strip()) for line in file]
    forward_increase = 0
    depth_increase = 0

    for i in range(0, len(input_array)):
        fields = input_array[i].split(" ")
        if fields[0] == "forward":
            forward_increase += int(fields[1])
        if fields[0] == "down":
            depth_increase += int(fields[1])
        if fields[0] == "up":
            depth_increase -= int(fields[1])

print("total forward: %d and depth: %d: " %(forward_increase, depth_increase))
print(forward_increase * depth_increase)



