#!/usr/bin/python
# This program counts up the number of vowels contained in the string s
def findVowels():
	vowels = 'aeiouAEIOU'
	numberOfVowels = 0;
	s = raw_input('Insert a string: ');
	print s
	for v in s:
		if v in vowels:
			numberOfVowels = numberOfVowels + 1;
	print "Number of vowels: %d" % numberOfVowels
findVowels()
