def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Store the count of occurrences in count[]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr[] contains sorted numbers according to the current digit
    for i in range(n):
        arr[i] = output[i]

def radixSort(arr,n):
    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Do counting sort for every digit. Note that instead of passing digit number, exp is passed. exp is 10^i where i is the current digit number
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
