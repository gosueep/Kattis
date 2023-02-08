# !"#$%&'()*+,-./

def decode(rune):

    val = 0
    for i in rune:
        val += dec[i]

    # print(rune, val)
    return val


# for i, x in enumerate('!"#$%&\'()*+,-./'):
#     dec[x] = i+1
#     enc[i+1] = x
# print(dec)
# print(enc)
dec = {'!': 1, '"': 2, '#': 3, '$': 4, '%': 5, '&': 6, "'": 7, '(': 8, ')': 9, '*': 10, '+': 11, ',': 12, '-': 13, '.': 14, '/': 15}
enc = {1: '!', 2: '"', 3: '#', 4: '$', 5: '%', 6: '&', 7: "'", 8: '(', 9: ')', 10: '*', 11: '+', 12: ',', 13: '-', 14: '.', 15: '/'}

special = {'0': ' ',
           '<': ',',
           '>': '.'}

rune, l = input().split()

og_pos = ord(l) - ord('a') + 1
shift = decode(rune) - og_pos

decoded = {}
for i, x in enumerate('abcdefghijklmnopqrstuvwxyz'):
    num = (i + 1 + shift) % 26
    decoded[num] = x

while True:
    try:
        line = input().split()
    except:
        break

    for i in line:

        if i in special:
            print(special[i], end='')
        else:
            print(decoded[decode(i) % 26], end='')
    print()


