def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	total=[]
	for i in a:
		sum =0
		if len(b) == len(i):
			for j in range(len(i)):
				sum += i[j] * b[j]
			total.append(sum)
		else:
			return -1
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	return total