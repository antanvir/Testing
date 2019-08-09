NoOfVariables = None
Boundaries = []
Labels = ["_min", "_max", "_min+", "_max-", "_min-", "_max+", "_nor"]
sampleValues = []
VariableStem = "X"
varName = []


def takeInputs():
    global NoOfVariables, Boundaries
    file = open("input1.txt", "r")
    data = file.readlines()
    for i in range(len(data)):
        data[i] = [int(x) for x in data[i].strip().split()]

    NoOfVariables = data[0][0]
    for i in range(1, len(data)):
        Boundaries.append(data[i])
    # print(data)
    print(NoOfVariables)
    print(Boundaries)


def sampleForOneVariable(lower, upper):
    values = [lower, upper, lower + 1, upper - 1,
              lower - 1, upper + 1, (lower + upper) // 2]
    return values


def chooseSampleValuesFromRange():
    for item in Boundaries:
        lower, upper = item[0], item[1]
        values = sampleForOneVariable(lower, upper)
        sampleValues.append(values)


def testNormalValueCase():
    global NoOfVariables, Boundaries, Labels, varName
    varName = ["X" + str(i) for i in range(NoOfVariables)]
    variables, values = "", ""
    for i in range(NoOfVariables):
        variables += varName[i] + Labels[6] + ", "
        values += str(sampleValues[i][6]) + ", "
    print("[1]", " ", variables.rstrip(", "), "\t", values.rstrip(", "))


def testOtherCasesForEachVariable(n):
    global NoOfVariables, Boundaries, Labels, varName
    for i in range(0, (n * NoOfVariables)):
        no = "[" + str(i + 2) + "]"
        variables, values = "", ""
        for j in range(NoOfVariables):
            index = 6
            if j == i // n:
                index = i % n
            variables += varName[j] + Labels[index] + ","
            values += str(sampleValues[j][index]) + ", "
        print(no, " ", variables.rstrip(", "), "\t", values.rstrip(", "))


def testBoundaryValues():
    print("\n[BOUNDARY VALUE CHECK]\n")
    testNormalValueCase()
    testOtherCasesForEachVariable(4)


def testRobustly():
    print("\n[ROBUST CHECKING]\n")
    testNormalValueCase()
    testOtherCasesForEachVariable(6)


def testWorstCases():
    global NoOfVariables, Boundaries, Labels, varName
    print("\n[WORST-CASE CHECK]\n")

    varName = ["X" + str(i) for i in range(NoOfVariables)]
    for i in range(0, pow(5, NoOfVariables)):
        no = "[" + str(i + 1) + "]"
        variables, values = "", ""
        res = i
        for j in range(NoOfVariables):
            index = res % 5
            if index == 4:
                index += 2
            variables += varName[j] + Labels[index] + ", "
            values += str(sampleValues[j][index]) + ", "
            res = res // 5
        print(no, " ", variables.rstrip(", "), "\t\t", values.rstrip(", "))


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
