def bin_search(arr, x):
	i = 0
	j = len(arr)
	found = False
	temp = -1
	while i < j-1 and not(found):
		try_indices = int((i+j)/2)
		if arr[try_indices] == x:
			temp = try_indices
			found = True
		elif arr[try_indices] < x :
			i = try_indices
		elif arr[try_indices] > x :
			j = try_indices
	return temp


m = [i for i in range(101)]
print(bin_search(m, 2))
print(bin_search(m, 101))
print(bin_search(m, 7))
print(bin_search(m, 460))