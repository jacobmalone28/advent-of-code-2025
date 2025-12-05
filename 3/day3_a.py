import subprocess

voltages = []

with open("input") as f:
    for line in f:
        max1 = -1
        max2 = -1
        for c in line[:-2]:
            if int(c) > max1:
                max1 = int(c)
                max2 = -1
            elif int(c) > max2:
                max2 = int(c)
        if int(line[-2]) > max2:
            max2 = int(line[-2])
        voltages.append(max1 * 10 + max2)

answer = str(sum(voltages))
subprocess.run("pbcopy", text=True, input=answer)
print(answer, "(copied to clipboard)")