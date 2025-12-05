import subprocess

spot = 50
count = 0

with open("input") as f:
  for line in f:
    direction = 1 if line[0] == "R" else -1
    amount = int(line[1:])
    spot = (spot + direction * amount) % 100
    if spot == 0:
      count += 1

answer = str(count)
subprocess.run("pbcopy", text=True, input=answer)
print(answer, "(copied to clipboard)")