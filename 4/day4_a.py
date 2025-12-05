import subprocess

grid = []
accessible = 0

with open("input") as f:
    for line in f:
        line = line.strip()
        row = []
        for c in line:
            row.append(c)
        grid.append(row)

for row_num in range(len(grid)):
    for col_num in range(len(grid[row_num])):
        if grid[row_num][col_num] == ".":
            continue
        
        # c is @
        num_around = 0
        if col_num > 0:
            if grid[row_num][col_num-1] == "@":
                num_around += 1
            if row_num > 0:
                if grid[row_num-1][col_num-1] == "@":
                    num_around += 1
                    
        if col_num < len(grid[0]) - 1:
            if grid[row_num][col_num+1] == "@":
                num_around += 1
            if row_num < len(grid) - 1:
                if grid[row_num + 1][col_num + 1] == "@":
                    num_around += 1
        if row_num > 0:
            if grid[row_num - 1][col_num] == "@":
                num_around += 1
            if col_num < len(grid[0]) - 1:
                if grid[row_num - 1][col_num + 1] == "@":
                    num_around += 1
        if row_num < len(grid) - 1:
            if grid[row_num + 1][col_num] == "@":
                num_around += 1
            if col_num > 0:
                if grid[row_num + 1][col_num - 1] == "@":
                     num_around += 1

        if num_around < 4:
            accessible += 1

answer = str(accessible)
subprocess.run("pbcopy", text=True, input=answer)
print(answer, "(copied to clipboard)")