c=int
for _ in '7'*c(input()):i,x=input().split();print(i,0 if'9'in x or'8'in x else c(x,8),c(x),c(x,16))