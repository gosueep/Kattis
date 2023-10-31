inp = input("")
out = []
printout = ""
count = 0
for i in inp:
    if i == "<":
        count += 1
    else:
        for j in range(count*2):
            out.pop()
        count = 0
    out.append(i)

while True:
    try:
        if out[-1] == "<":
            for j in range(count*2):
                out.pop()
        else:
            break
    except:
        break



print("".join(out))