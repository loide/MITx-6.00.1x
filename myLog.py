'''
This program computes the logarithm of a number relative to a base.
Inputs:
	number: the number to compute the logarithm
	base: the base of logarithm
Output:
	Logarithm value [ log_base (number) ]
'''

def myLog(number, base):
    if ( (type(number) != int) or (number < 0)):
        return "Error: Number value must be a positive integer."

    if ( (type(base) != int) or (base < 2)):
        return "Error: Base value must be an integer greater than or equal 2."

    return recursiveRad(number, base)


def recursiveRad(number, base):
    if base > number:
        return 0

    if number <= 1:
        return 0
    else:
        return 1 + recursiveRad(number/base, base)

if __name__ == "__main__":
    number = int(raw_input('Insert a number: '))
    base = int(raw_input('Insert the base value: '))
    print myLog(number, base)
