with open("day3/input.txt") as f:
    global_max = 0
    for line in f:
        line = line.strip()
        line_max = 0
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                val = int(line[i]) * 10 + int(line[j])
                if val > line_max:
                    line_max = val
        global_max += line_max

    print(global_max)
