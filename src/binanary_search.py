def binary_search(data, val):
	n = len(data)
	l = 0
	r = n-1
	while l<r:
		m = l+ (r-1)/2
		if data[m] == val:
			return m
		if data[m]<val:
			l = m+l
		elif data[m] > val:
			m = m - l
	return -1
			


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val2)