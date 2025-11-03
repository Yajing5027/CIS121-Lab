def hailstone_seq(n):
	# sequence = [n/n]	
	sequence = [n]
	
	# while n == 1:		
	while n != 1:
		if n % 2 == 0:
			# n = n // 2	
			n = n / 2
		else:
			# n = 2 * n + 1	
			n = 3 * n + 1
		sequence.append(n)
		
	return sequence

print(hailstone_seq(25))
