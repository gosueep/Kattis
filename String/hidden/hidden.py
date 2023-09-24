secret, password = input().split()

i=0
fail = False
for p in password:
    if p == secret[i]:
        i = (i+1) 
        if i >= len(secret):
            break
    elif p in secret[i:]:            
        fail = True

if fail or i < len(secret):
    print("FAIL")
else:
    print("PASS")            