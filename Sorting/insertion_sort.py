# Insertion Sort
def insertion_sort(arr): # Increasing Sort
	for i in range(1,len(arr)):
		end = i
		start = end
		temp = arr[end]
		for j in range(end,-1,-1):
			if arr[i] < arr[j]:
				start = j
		for k in range(end,start-1,-1):
			arr[k] = arr[k-1]
		arr[start] = temp
	return arr
