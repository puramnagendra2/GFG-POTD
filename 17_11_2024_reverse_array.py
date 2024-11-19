# Use Two Pointer Concept
def reverse_arr(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


# arr1 = list(map(int, input().split()))
arr = [1, 5, 4, 9, 3]
n = len(arr)
print(reverse_arr(arr))
