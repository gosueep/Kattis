x=input
for _ in'_'*int(x()):
 c=x();l,r=0,int(x());d=x()[1:-1].replace(',',' ').split();b=0
 for i in c:
  if'R'==i:b=-b+1
  else:r,l=[(r,l+1),(r-1,l)][b]
 d=d[l:r];print([f'[{",".join([d,d[::-1]][b])}]','error'][l>r])