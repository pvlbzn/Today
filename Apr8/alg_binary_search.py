# Attempt to implement the binary search

def search(n, arr):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = int(lo + (hi - lo) / 2)
        if n < arr[mid]:
            hi = mid - 1
        elif n > arr[mid]:
            lo = mid + 1
        else:
            return mid
    return -1

