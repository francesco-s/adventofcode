invalid_nums: int = 0

with open("day2/input.txt") as f:
    for line in f:
        line_splitted = line.split(",")
        for _range in line_splitted:
            range_min, range_max = _range.split("-")

            for num in range(int(range_min), int(range_max) + 1):
                num_str: str = str(num)
                num_len = len(num_str)

                if num_len % 2 == 1:
                    continue
                elif num_str[: num_len // 2] == num_str[num_len // 2 :]:
                    invalid_nums += num

print(invalid_nums)

# TODO: generate invalid IDs instead of checking every number
