N, k = map(int, input().split())
A = list(map(int, input().split()))
print(' '.join([str(A[i]) for i in range(k-1, N, k)]))