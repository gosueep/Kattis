# d='0123456789';p=[int(i+j+k+k+j+i)for i in d for j in d for k in d]
# for _ in'*'*int(input()):n=int(input());print(min(p,key=lambda x:abs(n-x)))


# p=[f'00{str(i)}'[-3:]for i in range(1000)]
# for _ in'*'*int(input()):n=int(input());print(min([int(i+i[::-1])for i in p],key=lambda x:abs(n-x)))

# for _ in'*'*int(input()):print(min([int(i+i[::-1])for i in[f'00{str(i)}'[-3:]for i in range(1000)]],key=lambda x:abs(int(input())-x)))
# for _ in'*'*int(input()):n=int(input());print(min([int(i+i[::-1])for i in[str(i)for i in range(1000)]],key=lambda x:abs(n-x)))
for _ in'*'*int(input()):n=int(input());print(min([int(str(i)+str(i)[::-1])for i in range(1000)],key=lambda x:abs(n-x)))

for _ in'*'*int(input()):n=int(input());print(min([int(str(i)+str(i)[::-1])for i in range(1000)],key=lambda x:abs(n-x)))
