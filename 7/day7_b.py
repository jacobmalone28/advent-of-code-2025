import subprocess

splits = 1

with open("input") as f:
    active_beams = {}
    lines = f.readlines()
    for col, char in enumerate(lines[0]):
        if char == "S":
            active_beams[col] = active_beams.get(col, 0) + 1
            break
    for line in lines[1:]:
        for col, char in enumerate(line):
            if char == "^" and col in active_beams:
                splits += active_beams[col]
                ways = active_beams.pop(col)
                active_beams[col-1] = active_beams.get(col-1, 0) + ways
                active_beams[col+1] = active_beams.get(col+1, 0) + ways

answer = str(splits)
subprocess.run("pbcopy", text=True, input=answer)
print(answer, "(copied to clipboard)")