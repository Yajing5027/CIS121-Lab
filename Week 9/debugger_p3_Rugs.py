def design_rug(width, length, pattern):
	result = "Your rug is:\n"
	# for i in range(length =1):		
	for i in range(length):
		result += pattern * width
		# if i < length = 1:		
		# result += "\t"		
		if i < length - 1:
			result += "\n"
	return result


# def design_rug(width, length, pattern):		
def design_rug(width, length, pattern = "@"):
	result = "Your rug is:\n"
	for i in range(length):
		result += pattern * width
		if i < length - 1:
			result += "\n"
	return result

print(design_rug(5,3))
