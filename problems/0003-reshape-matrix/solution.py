import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	reshaped_matrix=[]
	temp =[]
	for i in range(len(a)):
		for j in range(len(a[i])):
			temp.append(a[i][j])
	if len(temp) != new_shape[0] * new_shape[1]:
		return []
	
	for i in range(new_shape[0]):
		reshaped_matrix.append(temp[i*new_shape[1]:(i+1)*new_shape[1]])

	return reshaped_matrix