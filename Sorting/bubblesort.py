def bubblesort_test(arr):
	for i in range(len(arr)-1,-1,-1):
		pivot = arr[-1]
		for j in range(len(arr)-2,len(arr)-2-i,-1):
			if pivot < arr[j]:
				arr[j+1] = arr[j]
				arr[j] = pivot
			else:
				pivot = arr[j]
	return arr
