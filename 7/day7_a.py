import subprocess

splits = 0

with open("input") as f:
    active_beams = set()
    lines = f.readlines()
    for col, char in enumerate(lines[0]):
        if char == "S":
            active_beams.add(col)
            break
    for line in lines[1:]:
        for col, char in enumerate(line):
            if char == "^" and col in active_beams:
                splits += 1
                active_beams.remove(col)
                active_beams.add(max(0, col-1))
                active_beams.add(min(len(line)-1, col+1))
            

answer = str(splits)
subprocess.run("pbcopy", text=True, input=answer)
print(answer, "(copied to clipboard)")