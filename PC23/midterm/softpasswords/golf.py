s,a=[input()for _ in'**']
p=[a,''.join([i.lower()if i>'`'else i.upper() for i in a])]
for i in'0123456789':p+=[a+i,i+a]
[p+=[a+i,i+a]for i in'0123456789']
print(['No','Yes'][s in p])