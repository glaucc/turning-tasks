#test
def findErrorNums(nums):
	numbers = []
	for x in nums:
		numbers.append(x)
	result = []
	output = []
	#1,2,3,4
    val = len(numbers)
    val = val + 1
	for i in range(val):
		result.append(i)
	for j in numbers:
		for n in result:
			if j != n:
				output.append(j)
				output.append(n)
	return output

if __name__ == '__main__':
	line = input()
	components = line.strip().split()
	components = [int(component) for component in components]

	print(findErrorNums(components))