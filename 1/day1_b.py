spot = 50
count = 0

with open("input") as f:
  for line in f:
    direction = 1 if line[0] == "R" else -1
    amount = int(line[1:])
    for _ in range(amount):
        spot = (spot + direction) % 100
        if spot == 0:
            count += 1

print(count)