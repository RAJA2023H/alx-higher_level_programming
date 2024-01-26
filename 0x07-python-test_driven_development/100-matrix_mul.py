#!/usr/bin/python3
"""Module to find the max integer in a list
"""
def matrix_mul(m_a, m_b):
	result = []
	if len(m_a[0]) != len(m_b):
        	raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")

	for i in range(len(m_a)):
		row = []
		for j in range(len(m_b[0])):
			mul = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
			row.append(mul)
		result.append(row)
	return result
