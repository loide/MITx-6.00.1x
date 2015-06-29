#!/usr/bin/python
# This program 	prints the longest substring of 's' in which the letters
# occurs in alphabetical order. For example, if s='azcbobobegghakl', then
# the program will print: Longest substring in alphabetical order is: beggh
def findLongestSubstring():
	strings = []
	s = raw_input('Insert a string: ');
	print s

	substring = ''
	while (len(s) > 0):
		if ((len(substring) == 0) or (substring[-1] <= s[0])):
			substring = substring + s[0]
			s = s[1:len(s)]
		else:
			strings.append(substring)
			substring = ''
	strings.append(substring)
	print "Longest substring: %s" % sorted(strings, key=len, reverse=True)[0]
findLongestSubstring()
