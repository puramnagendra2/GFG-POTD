"""
You are given an integer array arr[].
Your task is to find the smallest positive number missing from the array.

Note: Positive number starts from 1. The array can have negative integers too.

Examples:

Input: arr[] = [2, -3, 4, 1, 1, 7]
Output: 3
Explanation: Smallest positive missing number is 3.
Input: arr[] = [5, 3, 2, 5, 1]
Output: 4
Explanation: Smallest positive missing number is 4.
Input: arr[] = [-8, 0, -1, -4, -3]
Output: 1
Explanation: Smallest positive missing number is 1.
Constraints:
1 <= arr.size() <= 10^5 (Can be O(n log n) or O(n)
-106 <= arr[i] <= 10^6
"""


def smallestPositiveNumber(nums):
    n = len(nums)

    # Rearranging numbers
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # Swap
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    # Finding the first missing positive
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


arr = [2, -3, 4, 1, 1, 7]
arr1 = [-8, -1, -4, -3]
arr1 = [1, 2, 0]
arr = [7, 8, 9]
print(smallestPositiveNumber(arr))
