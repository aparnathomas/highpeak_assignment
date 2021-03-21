# python version 3.7
numberOfEmployees = 0
goodiesList = {}
selectedGoodies = {}
rankList = {}
getNoOfEmpString = "Number of employees: "
flag = False
flagKey = 0
try:
    with open("D:\highpeak_assign\SimplePyFiles/sample_input2.txt", mode='r') as inputFile:
        for line in inputFile.readlines():
            if line.isspace():
                continue
            if flag:
                line = line.split(':')
                try:
                    line[1] = int(line[1].replace('\n', "").strip())
                    goodiesList[line[1]] = line[0]
                except:
                    print(line[0], " Price is not in Integer : Error")
                    break
            if "Goodies and Prices:" in line:
                flag = True
            if getNoOfEmpString in line:
                try:
                    numberOfEmployees = int(line[len(getNoOfEmpString)])
                except:
                    print("No: of Employees Must Present in Integer")
                    break
    # print(numberOfEmployees)
    # print(goodiesList)
    listOnlyPrice = list(goodiesList.keys())

    listOnlyPrice.sort()
    # print(listOnlyPrice)
    for i in range((len(listOnlyPrice))-numberOfEmployees+1):
        rankList[listOnlyPrice[i+numberOfEmployees-1]-listOnlyPrice[i]
                 ] = (listOnlyPrice[i], listOnlyPrice[i+numberOfEmployees-1])
    flagKey = min(list(rankList.keys()))
    # print(rankList)
    with open("D:\highpeak_assign\SimplePyFiles/sample_output2.txt", mode='w') as outputFile:
        outputFile.write("The goodies selected for distribution are:\n\n")
        outPutList = []
        rankRange = rankList[flagKey]
        # print(rankRange, " ", listOnlyPrice," " ,i )
        for i in range(listOnlyPrice.index(rankRange[0]), (listOnlyPrice.index(rankRange[1]))+1):
            outPutList.append(listOnlyPrice[i])
        # print(outPutList)
        for price in outPutList:
            outputFile.write(goodiesList[price]+" : "+str(price)+"\n")
        outputFile.write(
            "\nAnd the difference between the chosen goodie with highest price and the lowest price is "+str(flagKey))

except FileNotFoundError:
    print("Input File is not found")
finally:
    pass
