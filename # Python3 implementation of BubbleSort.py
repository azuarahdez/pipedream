# Optimized Python program for implementation of Bubble Sort
def bubbleSort(arr):
	n = len(arr)
	

	for i in range(n):
		swapped = False
	
		for j in range(0, n-i-1):
	
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
		if (swapped == False):
			break

if __name__ == "__main__":
	arr = [24, 10, 2, 4, 1, 100, 45, 64, 71, 66, 28, 58, 33]

	bubbleSort(arr)

	print("Sorted array:")
	for i in range(len(arr)):
		print("%d" % arr[i], end=" ")

