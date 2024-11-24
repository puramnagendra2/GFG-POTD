"""
Given an integer array arr[]. You need to find the maximum sum of a subarray.

Examples:

Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.
Input: arr[] = [-2, -4]
Output: -2
Explanation: The subarray {-2} has the largest sum -2.
Input: arr[] = [5, 4, 1, 7, 8]
Output: 25
Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.
Constraints:
1 ≤ arr.size() ≤ 10^5
-109 ≤ arr[i] ≤ 10^4
"""


def maxSubArraySum(arr):
    n = len(arr)
    maxi = -1e8
    currSum = 0
    for i in range(0, n):
        currSum = currSum + arr[i]
        if (currSum > maxi):
            maxi = currSum
        if (currSum < 0):
            currSum = 0
    return maxi


arr = [2, 3, -8, 7, -1, 2, 3]
print(maxSubArraySum(arr))
