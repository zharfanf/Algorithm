# Selection Sort
def selection_sort(arr): # Increase sort
	for i in range(len(arr)-1):
		Imax = i
		for j in range(i+1,len(arr)):
			if arr[Imax] > arr[j]:
				Imax = j
		temp = arr[i]
		arr[i] = arr[Imax]
		arr[Imax] = temp
	return arr
