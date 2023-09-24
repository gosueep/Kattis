s,h=input().split();i,p,l=0,0,len(s)
for p in h:
 if s[i%l]==p:i+=1
 elif p in s[i:]:break
print("PFAASISL"[i<l::2])