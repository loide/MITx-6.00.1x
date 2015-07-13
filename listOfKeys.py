'''
This function returns a list of keys in a dictionary aDict with value target.
Inputs:
	aDict: an dictionary
	target: an integer
Output:
	returns a list (empty list if target is not found)
'''

def listOfKeys(aDict, target):
    keysWithValue = []

    for x, y in aDict.items():
	if y == target:
            keysWithValue.append(x)
    keysWithValue.sort()

    return keysWithValue
		

if __name__ == "__main__":
    aDict = {0: 3, 1: 4, 2: 5, 3: 4, 5: 4, 6: 5, 7: 5, 8: 4, 9: 3, 10: 4}
    target = 0
    print listOfKeys(aDict, target)
