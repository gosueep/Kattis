import re

line = input()

for smile in [':\)', ';\)', ':-\)', ';-\)']:
    smiles = re.split(smile, line)

    if len(smiles) > 1:
        address = 0
        for s in smiles[:-1]:
            address += len(s)
            print(address)
            address += len(smile) - 1


