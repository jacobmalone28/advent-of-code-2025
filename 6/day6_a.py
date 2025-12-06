import subprocess

nums = []
answers = []

with open("input") as f:
    lines = list(map(lambda f: f.split(), f.readlines()))
    nums = [[] for i in range(len(lines[0]))]
    answers = [0] * len(lines[0])
    
    for line in lines[:-1]:
        for i in range(len(line)):
            nums[i].append(int(line[i]))
    
    for i, op in enumerate(lines[-1]):
        match op:
            case "+":
                for n in nums[i]:
                    answers[i] += n
                
            case "*":
                answers[i] = 1
                for n in nums[i]:
                    answers[i] *= n
    
answer = str(sum(answers))
subprocess.run("pbcopy", text=True, input=answer)
print(answer, "(copied to clipboard)")