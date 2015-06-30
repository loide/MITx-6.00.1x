"""
This program calculate base^exp using recursion and multiplication and remainder
base^exp = ( base^2 )^( exp/2 ) if exp > 0 and exp is even
base^exp = base * base^(exp - 1) if exp > 0 and exp is odd
base^exp = 1 if exp == 0
"""

def recursivePowerNew(base, exp):
    if exp == 0:
        return 1
    if (exp > 0):
        if ((exp % 2) > 0):
            return base * recursivePowerNew(base, exp - 1)
        else:
            return recursivePowerNew(base * base, exp / 2)

if __name__ == "__main__":
    print recursivePowerNew(9, 3)
