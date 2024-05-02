while True:
    N = int(input())
    
    pile1 = 0   # stack to take in order from
    pile2 = 0   # stack to pile on
    
    for _ in range(N):
        instr, amt = input().split()
        amt = int(amt)
        if instr == 'DROP':
            pile2 += amt
            print('DROP', 2, amt)
        elif instr == 'TAKE':
            if pile1 < amt:
                move = amt-pile1
                pile2 -= move
                pile1 += move
                print('MOVE 2->1', move)
            pile1 -= amt
             