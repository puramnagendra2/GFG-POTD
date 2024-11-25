"""
Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr.

Note: It is guaranteed that the output fits in a 32-bit integer.

Examples

Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180
Explanation: The subarray with maximum product is {6, -3, -10} with product = 6 * (-3) * (-10) = 180.
Input: arr[] = [-1, -3, -10, 0, 60]
Output: 60
Explanation: The subarray with maximum product is {60}.
Input: arr[] = [2, 3, 4]
Output: 24
Explanation: For an array with all positive elements, the result is product of all elements.
Constraints:
1 ≤ arr.size() ≤ 10^6
-10  ≤  arr[i]  ≤  10
"""


def maxSubarrayProduct(arr):
    maxi, mini, maxP = arr[0], arr[0], arr[0]
    for i in range(1, len(arr)):
        if arr[i] < 0:
            maxi, mini = mini, maxi
        maxi = max(arr[i], maxi*arr[i])
        mini = min(arr[i], mini*arr[i])
        maxP = max(maxi, maxP)
    return maxP


arr = [-2, 6, -3, -10, 0, 2]
arr = [-1, -3, -10, 0, 60]
arr = [2, 3, 4]
arr = [4, 10, -9, -1, 9, -9, 9, 5, -4]
print(maxSubarrayProduct(arr))



