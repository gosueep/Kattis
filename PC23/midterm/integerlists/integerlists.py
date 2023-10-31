from collections import deque

for _ in range(int(input())):
    instrs = input().strip()
    n = int(input())
    inp = input()[1:-1].split(',')
    nums = deque()
    for i in inp:
        if i != '':
            nums.append(int(i))
    
    rev = False
    err = False
    for i in instrs:
        if i == 'R':
            rev = not rev
        elif i == 'D':
            if len(nums) == 0:
                err = True
                break
            if rev: nums.pop()
            else: nums.popleft()
    if err:
        print('error')
    else:
        if rev:
            nums = reversed(nums)
        print('[' + ','.join(str(x) for x in nums) + ']')