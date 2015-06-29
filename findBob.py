#!/usr/bin/python
# This program find the number of times the substring 'bob' occurs in the string 's'
def findBob():
	numberOfBobs = 0;
	s = raw_input('Insert a string: ');
	print s
	while (len(s) > 3):
		index = s.find('b')
		if (index < 0):
			break
		if s[index:index+3] == 'bob':
			numberOfBobs = numberOfBobs + 1
		s = s[index+1:len(s)]
	print "Number of times bob occurs is: %d" % numberOfBobs
findBob()
