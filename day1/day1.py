input_file_name = "./day1/input.txt"
input_sample_file_name = "./day1/input_sample.txt"

input = open(input_file_name, 'r').read().strip().split('\n')


# Part 1
start = 50

how_many_zeros = 0

for line in input:
    directions = line[0]
    distance = int(line[1:].strip())
    if directions == 'L':
        move = start - distance
    elif directions == 'R':
        move = start + distance

    move = move % 100

    start = move
    if start == 0:
        how_many_zeros += 1

print(how_many_zeros)


# Part 2
start = 50
how_many_zeros = 0

for line in input:
    direction = line[0]
    distance = int(line[1:].strip())

    for steps in range(distance):
        if direction == 'R':
            start += 1
        else:
            start -= 1

        if start % 100 == 0:
            how_many_zeros += 1

    start = start % 100

print(how_many_zeros)