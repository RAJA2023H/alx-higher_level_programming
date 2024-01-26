#!/usr/bin/python3
"""Module to find the max integer in a list
"""
def matrix_mul(m_a, m_b):
	result = []

	if len(m_a[0]) != len(m_b):
        	raise ValueError("m_a and m_b can't be multiplied")

	if not isinstance(m_a, list):
		raise TypeError ( "m_a must be a list")
	if not isinstance(m_a, list):
                raise TypeError ( "m_b must be a list")

	if not all(isinstance(row, list) for row in m_a):
		raise TypeError ("m_a must be a list of lists")
	if not all(isinstance(row, list) for row in m_a):
                raise TypeError ("m_b must be a list of lists")

	if m_a == [] or m_a = [[]]:
                raise TypeError ("m_a can't be empty")
	if m_b == [] or m_b = [[]]:
		raise TypeError ("m_b can't be empty")

	if not all(isinstance(element, (int, float)) for row in m_a for element in row):
		raise TypeError ("m_a should contain only integers or floats")
	if not all(isinstance(element, (int, float)) for row in m_b for element in row):
                raise TypeError ("m_b should contain only integers or floats")

	if not all(len(row) == len(m_a[0])for row in m_a[1:])
		raise TypeError ("each row of m_a must be of the same size")		
	if not all(len(row) == len(m_b[0])for row in m_b[1:])
                raise TypeError ("each row of m_b must be of the same size")

	if len(m_a[0]) != len(m_b):
                raise ValueError("m_a and m_b can't be multiplied")
	for i in range(len(m_a)):
		row = []
		for j in range(len(m_b[0])):
			mul = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
			row.append(mul)
		result.append(row)
	return result
