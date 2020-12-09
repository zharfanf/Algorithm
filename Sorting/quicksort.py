def partitioning(arr,start,end):
	i = start-1
	j = start
	pivot = arr[end-1]
	while j < end-1:
		if arr[j] < pivot:
			i += 1
			arr[i],arr[j] = arr[j],arr[i] #swap element
		j += 1		
	p = i + 1
	arr[p],arr[end-1] = arr[end-1],arr[p] #swap pivot and element on i+1
	return p


def quicksort(arr,start,end):
	if start >= end: # return nothing
		return
	examine = partitioning(arr,start,end)
	quicksort(arr,start,examine)
	quicksort(arr,examine+1,end)
	return arr

