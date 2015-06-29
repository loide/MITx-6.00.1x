#! /usr/bin/python
# This program calculate the credit card balance after one year if a person pays the minimum monthly
# payment required by the credit card company each month.
# Inputs:
#	balance : the outstanding balance on the credit card
#	annualInterestRate: annual interest rate as a decimal
#	monthlyPaymentRate: minimum monthly payment rate as a decimal

def calculateCreditCard():
	balance = raw_input('Outstanding balance on the credit card :')
	annualInterestRate = raw_input('Annual Interest Rate:')
	monthlyPaymentRate = raw_input('Minimum Monthly Payment Rate:')
	month = 1
	monthlyInterestRate = float(annualInterestRate) / 12.0
	balance = float(balance)
	monthlyPaymentRate = float(monthlyPaymentRate)
	totalPaid = 0

	while month < 13:
		minimumPayment = balance * monthlyPaymentRate
		monthlyUnpaidBalance = balance - minimumPayment
		balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
		totalPaid = totalPaid + minimumPayment

		print "-----------------------------------------------------------"
		print "Month: %d " % month
		print "Minimum monthly payment: %.2f" % minimumPayment
		print "Remaining balance: %.2f" % balance
		month = month + 1

	print "-------------------------------------------------------------"
	print "Total paid: %.2f" % totalPaid
	print "Remaining balance: %.2f" % balance
calculateCreditCard()
