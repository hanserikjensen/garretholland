def odd_even():
	even = "number is {}. This is an even number"
	odd = "number is {}. This is an odd number"
	for num in range(2001):
		if num % 2 == 0:
			print even.format(num)
		else:
			print odd.format(num)

odd_even()
