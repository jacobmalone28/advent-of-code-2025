import subprocess

invalid = []

with open("input") as f:
    ranges = f.read().split(",")
    for r in ranges:
        b_and_e = r.split("-")
        b = int(b_and_e[0])
        e = int(b_and_e[1])
        for i in range(b,e+1):
            s = str(i)
            if (s + s).index(s, 1) != len(s):
                invalid.append(i)

answer = str(sum(invalid))
subprocess.run("pbcopy", text=True, input=answer)
print(answer, "(copied to clipboard)")