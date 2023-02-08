# https://open.kattis.com/problems/queens

if __name__ == '__main__':
    N = int(input())

    board = [[0 for y in range(N)] for x in range(N)]

    ranks = set()
    files = set()
    diag1 = set()
    correct= True

    for _ in range(N):
        rank, file = map(int, input().split())

        if rank in ranks or file in files:
            correct = False
            break

        ranks.add(rank)
        files.add(file)

        diag1.add(3)



        r = rank
        f = file
        while 0 < r < N and 0 < f < N:


    print('CORRECT') if correct else print('INCORRECT')