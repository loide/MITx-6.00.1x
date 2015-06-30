"""
This program calculates the Greatest Commom Divisor (GCD) of two positive 
integers using Euclid's Algorithm.
GCD is the largest integer that divides each of them without remainder.
"""

def recursiveGreatestCommonDivisor(a, b):
    if b == 0:
        return a
    return recursiveGreatestCommonDivisor(b, a % b)

if __name__ == "__main__":
    print recursiveGreatestCommonDivisor(12, 144)
