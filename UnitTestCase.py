NoOfVariables = None
BoundaryValues = []
Labels = ["_normal", "_min", "_max", "_min+", "_max-", "_min-", "_max+"]
VariableStem = "X"

def takeInputs():
	global NoOfVariables, BoundaryValues
	file = open("input.txt", "r")
	data = file.readlines()
	for i in range(len(data)):
		data[i] = [int(_) for _ in data[i]]


	NoOfVariables = data[0]
	for i in range(1, len(data)):
		BoundaryValues.append(data[i])

def generateTestCases():
	print("[SAMPLE TEST CASES]\n")
	global NoOfVariables, BoundaryValues, Labels, VariableStem

	for i in range(0, pow(7, NoOfVariables)):
		""

def main():
	takeInputs()
	generateTestCases()

if __name__ == "__main__":
    main()