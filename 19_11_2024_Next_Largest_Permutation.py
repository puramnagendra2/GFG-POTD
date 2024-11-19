"""
Given an array of integers arr[] representing a permutation,
implement the next permutation that rearranges the numbers into the lexicographically next greater permutation.
If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order).

Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.

Examples:

Input: arr = [2, 4, 1, 7, 5, 0]
Output: [2, 4, 5, 0, 1, 7]
Explanation: The next permutation of the given array is {2, 4, 5, 0, 1, 7}.
Input: arr = [3, 2, 1]
Output: [1, 2, 3]
Explanation: As arr[] is the last permutation, the next permutation is the lowest one.
Input: arr = [3, 4, 2, 5, 1]
Output: [3, 4, 5, 1, 2]
Explanation: The next permutation of the given array is {3, 4, 5, 1, 2}.
Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105
"""


def nextLargestPermutation(arr):
    i = len(arr) - 1
    while i >= 0 and arr[i] <= arr[i - 1]:
        i -= 1
    if i == 0:
        arr.reverse()
        return arr
    else:
        i -= 1
        idx = i + 1
        for k in range(idx, len(arr)):
            if (arr[i] < arr[k]) and (arr[idx] >= arr[k]):
                idx = k
        arr[i], arr[idx] = arr[idx], arr[i]
        arr[i + 1:] = reversed(arr[i + 1:])
        return arr


arr = list(map(int, input("Enter array elements ").split()))
print(nextLargestPermutation(arr))
