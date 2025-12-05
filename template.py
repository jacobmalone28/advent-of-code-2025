import subprocess

with open("input") as f:
    pass

answer = ""
subprocess.run("pbcopy", text=True, input=answer)
print(answer, "(copied to clipboard)")