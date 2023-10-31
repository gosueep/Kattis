for _ in'*'*int(input()):N,*A=map(int,input().split());print(f'{100*sum([i>sum(A)/N for i in A])/N:.3f}%')


100*sum([i>sum(A)/N for i in A])/N
