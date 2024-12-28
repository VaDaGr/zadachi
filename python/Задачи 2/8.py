def reverser(string):
	res = list(string.swapcase())
	res.reverse()
	return ''.join(res)

print(reverser("LUFITUAEB DNA GNUOY REGNOL ON M'i NEHW EM EVOL LLITS UOY LLIw"))