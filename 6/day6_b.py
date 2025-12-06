import subprocess

nums = []
answers = []

with open("input") as f:
    lines =  f.readlines()
    op_count = len(lines[0].split())
    nums = [["" for i in range(len(lines)) ] for i in range(op_count)]
    answers = [0] * op_count
    curr = 0
    num_col = 0
    
    for col in range(len(lines[0])):
        next_num = True
        for row, line in enumerate(lines[:-1]):
            if line[col] != " ":
                next_num = False
            nums[curr][num_col] += line[col]
            
        if next_num:
            curr += 1
            num_col = 0
        else:
            num_col += 1
    
    for i, operation in enumerate(lines[-1].split()):
        if operation == "*":
            answers[i] = 1
        for num in nums[i]:
            number = num.strip()
            if number:
                if operation == "+":
                    answers[i] += int(number)
                else:
                    answers[i] *= int(number)

answer = str(sum(answers))
subprocess.run("pbcopy", text=True, input=answer)
print(answer, "(copied to clipboard)")