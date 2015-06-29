#! /usr/bin/python
# This program calculate the minimum fixed monthly payment needed in order to pay off a credit
# card balance within 12 months.
# Inputs:
#	balance: the outstanding balance on credit card
#	annualInterestRate: annual interest rate as a decimal

def calculateDebtOffInAnYear():
	balance = raw_input('Outstanding balance on the credit card :')
	annualInterestRate = raw_input('Annual Interest Rate:')
	monthlyInterestRate = float(annualInterestRate) / 12.0
	balance = float(balance)
	minimumPayment = 0
	balanceFlag = True

	while balanceFlag:
		tmpBalance = balance
		minimumPayment = minimumPayment + 10.0

		for month in range(1,13):
			monthlyUnpaidBalance = tmpBalance - minimumPayment
			tmpBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

		if tmpBalance < 0:
			balanceFlag = False

	print "Lowest Payment: %d" % minimumPayment
calculateDebtOffInAnYear()
