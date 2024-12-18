def max_heapify(arr, n, i):
    largest = i        # Initialize largest as root
    left = 2 * i + 1   # Left child
    right = 2 * i + 2  # Right child

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Recursively heapify the affected subtree
        max_heapify(arr, n, largest)


def build_max_heap(arr):
    n = len(arr)
    # Start from last non-leaf node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)


def heapsort(arr):
    n = len(arr)
    build_max_heap(arr)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move current root to end
        max_heapify(arr, i, 0)           # Call max_heapify on the reduced heap


# Example:
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
heapsort(arr)
print("Sorted array:", arr)
