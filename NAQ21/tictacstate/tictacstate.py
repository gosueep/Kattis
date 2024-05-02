N = int(input())

for _ in range(N):
    oct = input()
    dec = int(oct, 8)
    game = bin(dec)[2:]

    game = '0'*(19-len(game)) + game
    
    turn = game[0]
    moves = game[1:-9]
    played = game[-9:]
    
    # print(game)
    # print(turn, moves, played)
    
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (6,4,2)]
    
    win = False
    for w in wins:
        if all([('1' == moves[a]) and (played[a] == '1') for a in w]):
            print('X wins')
            win = True
            break
        if all([('0' == moves[a]) and (played[a] == '1') for a in w]):
            print('O wins')
            win = True
            break
    
    if not win:
        if played == '1'*9:
            print('Cat\'s')
        else:
            print('In progress')
        