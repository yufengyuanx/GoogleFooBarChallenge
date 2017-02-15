def answer(s):
	total = 0
	for i in range(len(s)):
		if s[i] == '>':
			total = total + s[i:].count('<') * 2
	return total

