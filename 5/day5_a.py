import subprocess

ranges = []
amount = 0

with open("input") as f:
    line = f.readline()
    while line != "\n":
        b_e = line.split("-")
        ranges.append((int(b_e[0]),int(b_e[1])))
        line = f.readline()
    line = f.readline()
    while line != "":
        ingredient = int(line)
        for range in ranges:
            if ingredient >= range[0] and ingredient <= range[1]:
                amount += 1
                break
        line = f.readline()
    
answer = str(amount)
subprocess.run("pbcopy", text=True, input=answer)
print(answer, "(copied to clipboard)")