#! /usr/bin/python
# This program calculate the minimum fixed monthly payment needed in order to pay off a credit
# card balance within 12 months. This solution uses Bisection Search
# Inputs:
#	balance: the outstanding balance on credit card
#	annualInterestRate: annual interest rate as a decimal

def calculateDebtUsingBisectionSearch():
	balance = raw_input('Outstanding balance on the credit card :')
	annualInterestRate = raw_input('Annual Interest Rate:')
	monthlyInterestRate = float(annualInterestRate) / 12.0
	balance = float(balance)
	balanceFlag = True

	lowerBound = balance / 12.0
	upperBound = (balance * (1 + monthlyInterestRate)**12)/12.0
	minimumPayment = 0

	while True:
		tmpBalance = balance
		minimumPayment = (lowerBound + upperBound) / 2.0
		for month in range(1,13):
			monthlyUnpaidBalance = tmpBalance - minimumPayment
			tmpBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

		if (tmpBalance < 0.0):
			upperBound = minimumPayment
		elif (tmpBalance > 0.01):
			lowerBound = minimumPayment
		else:
			break

	print "Lowest Payment: %.2f" % minimumPayment
calculateDebtUsingBisectionSearch()
