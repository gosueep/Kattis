#Week 1 Problem A: Which Base is it Anyway?


numSets = int(input())
inputList = []
finalPrintables = []
#Print new line for every input
for i in range(numSets):
    nonSplitList = input()
    setNum, numToConvert = nonSplitList.split()
    setNum = int(setNum)
    numToConvert = int(numToConvert)
    inputList.append([setNum, numToConvert])

#Convert Octal to Decimal

for i in range(len(inputList)):
    octToDecimal = 0
    exponent = 0
    numToConvertCopy = inputList[i][1]
    while numToConvertCopy != 0:
        bit = numToConvertCopy % 10
        numToConvertCopy = int(numToConvertCopy / 10)
        if bit == 9:
            octToDecimal = 0
            break
        else:
            octToDecimal += (bit * 8**exponent)
            exponent += 1
    
    # print(octToDecimal)

    numToConvertCopy = inputList[i][1]
    #convert to decimal from hex
    hexToDecimal = 0
    exponent = 0
    while numToConvertCopy != 0:
        bit = numToConvertCopy % 10
        numToConvertCopy = int(numToConvertCopy / 10)
        hexToDecimal += (bit * 16**exponent)
        exponent += 1

    finalPrintables.append(f"{inputList[i][0]} {octToDecimal} {inputList[i][1]} {hexToDecimal}")


for i in finalPrintables:
    print(i)