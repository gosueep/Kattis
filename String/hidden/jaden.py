line = input().split()

password = []
message = []

for i in line[0]:
    password.append(i)

for j in line[1]:
    message.append(j)

valid = False



for letter in message:
    if letter in password:
        if password.index(letter) != 0:
            valid = False
            break

        elif password.index(letter) == 0 and len(password) > 0:
            password.pop(0)

    if len(password) == 0:
        valid = True
        break



if valid:
    print("PASS")
else:
    print("FAIL")
