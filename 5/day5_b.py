import subprocess

ranges = []

with open("input") as f:
    line = f.readline().strip()
    while line != "":
        start, end = map(int, line.split("-"))
        ranges.append([start, end])
        line = f.readline().strip()

ranges.sort()

merged_ranges = []
for start, end in ranges:
    if not merged_ranges or merged_ranges[-1][1] < start - 1:
        # No overlap with previous range
        merged_ranges.append([start, end])
    else:
        # Overlap with previous range, merge them
        merged_ranges[-1][1] = max(merged_ranges[-1][1], end)

answer = 0
for start, end in merged_ranges:
    count = end - start + 1
    answer += count
    print(f"Range {start}-{end}: {count} IDs")

print(f"\nTotal fresh ingredient IDs: {answer}")

answer = str(answer)
subprocess.run("pbcopy", text=True, input=answer)
print(f"{answer} (copied to clipboard)")