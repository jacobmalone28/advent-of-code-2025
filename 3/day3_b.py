voltages = []

with open("input") as f:
    for line in f:
        digits = []
        start = 0
        
        for i in range(12, 0, -1):
            
            maximum = -1
            new_start = 0
            for i, c in enumerate(line[start:-i]):
                # print(c, start, maximum, new_start)
                num = int(c)
                if num > maximum:
                    maximum = num
                    new_start = start + i
                    
            start = new_start + 1
            digits.append(str(maximum))   
        voltages.append(int("".join(digits)))

print(sum(voltages))


