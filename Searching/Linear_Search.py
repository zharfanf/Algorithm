def linear_search_for_loop(arr, x): # For Loop
	indices = -1
	for i in range(len(arr)):
		if arr[i] == x:
			indices = i
	return indices

def linear_search_while_do_loop(arr, x): # While Do Loop
	indices = -1
	i = 0; j = len(arr); found = False
	while i < j and not(found) :
		if arr[i] == x:
			indices = i
			found = True
		else :
			i += 1
	return indices