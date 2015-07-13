'''
This program takes a number, non-negative integer, and calculates the sum
of its digits.
Inputs:
	number: non-negative integer
Output:
	returns an integer ( the sum)
'''

def sumOfDigits(number):
    if ( (type(number) != int) or (number < 0)):
        return "Error: Number value must be a positive integer."

    return recursiveSum(number)


def recursiveSum(number):
    if number < 10:
        return number
    else:
        return (number % 10) + recursiveSum(number/10)

if __name__ == "__main__":
    number = int(raw_input('Insert a number: '))
    print sumOfDigits(number)
