#! /usr/bin/python
# This program works as follows: the user thinks of an integer between 0 and 100
# The computer makes guesses, and the user give it input - is it too high or too low?
# Using bisection search, the computer will guesses the user's secret number

def guessANumber():
	print 'Please think of a number between 0 and 100!'
	low = 0
	high = 100

	while True:
		ans = (high + low) / 2
		print 'Is your secret number ' + str(ans) + '?'
		option = raw_input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.')
		if option == 'l':
			low = ans
		elif option == 'h':
			high = ans
		elif option == 'c':
			break
		else:
			print 'Sorry, I did not understand your input.'
	print 'Game over. Your secret number was:' + str(ans)
guessANumber()
