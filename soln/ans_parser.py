import sys
print(sys.argv)
ans_raw = open(sys.argv[1]).readlines()

grid = []

for r in ans_raw:
    r = r.strip().split(' ')
    grid.append(r)

curr = 1

def find(n):
    ri, ci = (0, 0)
    for r in grid:
        ci = 0
        for c in r:
            if c.strip() == str(n):
                return (ri, ci)
            ci += 1
        ri += 1
    return None

print(find(1))
diffs = []
while curr < 64:
    next = curr + 1

    ci = find(curr)
    ni = find(next)

    diff = (ci[0]-ni[0], ci[1]-ni[1])
    diffs.append((diff[1], diff[0]))

    curr = next

offsets = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
dirs = []

for diff in diffs:
    idx = offsets.index(diff) + 1
    dirs.append(idx)
[print(x, end='') for x in dirs]