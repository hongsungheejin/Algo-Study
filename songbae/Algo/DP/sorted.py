def printUnsorted(arr, n):
    e = n-1
    # step 1(a) of above algo
    for s in range(0, n-1):
        if arr[s] > arr[s+1]:
            break

    if s == n-1:
        print("The complete array is sorted")
        exit()

    # step 1(b) of above algo
    e = n-1
    while e > 0:
        if arr[e] < arr[e-1]:
            break
        e -= 1

    # step 2(a) of above algo
    max = arr[s]
    min = arr[s]
    for i in range(s+1, e+1):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]

    # step 2(b) of above algo
    for i in range(s):
        if arr[i] > min:
            s = i
            break

    # step 2(c) of above algo
    i = n-1
    while i >= e+1:
        if arr[i] < max:
            e = i
            break
        i -= 1

    # step 3 of above algo
    print("The unsorted subarray which makes the given array")
    print((s,e))


arr = [1,3,2,4,5,6,7,8,9,10]
arr_size = len(arr)
printUnsorted(arr, arr_size)
