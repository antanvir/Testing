NoOfVariables = None
Boundaries = []
Labels = ["_min", "_max", "_min+", "_max-", "_min-", "_max+", "_nor"]
sampleValues = []
VariableStem = "X"
varName = []

def takeInputs():
    global NoOfVariables, Boundaries
    file = open("input.txt", "r")
    data = file.readlines()
    for i in range(len(data)):
        data[i] = [int(x) for x in data[i].strip().split()]


    NoOfVariables = data[0][0]
    for i in range(1, len(data)):
        Boundaries.append(data[i])
    # print(NoOfVariables)
    # print(data)
    # print(Boundaries)


def sampleForOneVariable(lower, upper):
    values = [lower, upper, lower + 1, upper - 1, lower - 1, upper + 1, (lower + upper) // 2]
    return values


def chooseSampleValuesFromRange():
    for item in Boundaries:
        lower, upper = item[0], item[1]
        values = sampleForOneVariable(lower, upper)
        sampleValues.append(values)
        # print(lower, " ", upper)
        # print(values)


def testBoundaryValues():
    print("\n[BOUNDARY VALUE CHECK]\n")
    global NoOfVariables, Boundaries, Labels, varName
    varName = ["X"+str(i) for i in range(NoOfVariables)]
    variables, values = "", ""
    for i in range(NoOfVariables):
        variables += varName[i]+Labels[6]+", "
        values += str(sampleValues[i][6])+", "
    print("[1]", " ", variables.rstrip(", "), "\t", values.rstrip(", "))


    for i in range(0, (4*NoOfVariables)):
        no = "[" + str(i+2) + "]"
        variables, values = "", ""
        for j in range(NoOfVariables):
            if j == i//4:
                variables += varName[j]+Labels[i % 4]+", "
                values += str(sampleValues[j][i % 4])+", "
            else:
                variables += varName[j]+Labels[6]+","
                values += str(sampleValues[j][6])+", "
        print(no, " ", variables.rstrip(", "), "\t", values.rstrip(", "))


def testRobustly():
    print("\n[ROBUST CHECKING]\n")
    global NoOfVariables, Boundaries, Labels, varName
    varName = ["X"+str(i) for i in range(NoOfVariables)]
    variables, values = "", ""

    for i in range(NoOfVariables):
        variables += varName[i]+Labels[6]+", "
        values += str(sampleValues[i][6])+", "
    print("[1]", " ", variables.rstrip(", "), "\t", values.rstrip(", "))


    for i in range(0, (6*NoOfVariables)):
        no = "[" + str(i+2) + "]"
        variables, values = "", ""
        for j in range(NoOfVariables):
            if j == i//6:
                variables += varName[j]+Labels[i % 6]+", "
                values += str(sampleValues[j][i % 6])+", "
            else:
                variables += varName[j]+Labels[6]+","
                values += str(sampleValues[j][6])+", "
        print(no, " ", variables.rstrip(", "), "\t", values.rstrip(", "))

def testWorstCases():
    ""



def generateTestCases():
    testBoundaryValues()
    testRobustly()
    testWorstCases()
    

def main():
    takeInputs()
    chooseSampleValuesFromRange()
    generateTestCases()

if __name__ == "__main__":
    main()