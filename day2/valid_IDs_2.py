invalid_nums: int = 0


def is_invalid(num_str: str, L: int) -> bool:
    for k in range(1, L):
        if L % k != 0:
            continue
        block = num_str[:k]
        if block * (L // k) == num_str:
            return True
    return False


with open("day2/input.txt") as f:
    for line in f:
        line_splitted = line.split(",")
        for _range in line_splitted:
            range_min, range_max = _range.split("-")

            for num in range(int(range_min), int(range_max) + 1):
                num_str: str = str(num)
                num_len = len(num_str)

                if is_invalid(num_str, num_len):
                    invalid_nums += num


print(invalid_nums)
