pos = 50
count0 = 0

with open("day1/input.txt") as f:
    content = f.read().strip()
lines = [ln.strip() for ln in content.splitlines() if ln.strip()]

for ln in lines:
    dirc = ln[0].upper()
    d = int(ln[1:])
    if dirc == "R":
        pos = (pos + d) % 100
    else:
        pos = (pos - d) % 100
    if pos == 0:
        count0 += 1

print(count0)
