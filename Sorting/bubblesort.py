def is_sort(arr):
	sort = True
	i = 1
	while sort and i < len(arr):
		if arr[i-1] > arr[i]:
			sort = False
		i += 1
	return sort


def bubblesort(arr):
	while not(is_sort(arr)):
		pivot = arr[-1]
		for i in range(len(arr)-2,-1,-1):
			if pivot < arr[i]:
				arr[i+1] = arr[i]
				arr[i] = pivot

			else:
				pivot = arr[i]
	return arr

print(bubblesort([7,1,3,0,9,8,4]))