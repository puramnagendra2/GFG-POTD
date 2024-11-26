"""
Given an array of integers arr[] in a circular fashion. Find the maximum subarray sum that we can get if we assume the array to be circular.

Examples:

Input: arr[] = [8, -8, 9, -9, 10, -11, 12]
Output: 22
Explanation: Starting from the last element of the array, i.e, 12,
and moving in a circular fashion, we have max subarray as 12, 8, -8, 9, -9, 10, which gives maximum sum as 22.

Input: arr[] = [10, -3, -4, 7, 6, 5, -4, -1]
Output: 23
Explanation: Maximum sum of the circular subarray is 23. The subarray is [7, 6, 5, -4, -1, 10].

Input: arr[] = [-1, 40, -14, 7, 6, 5, -4, -1]
Output: 52
Explanation: Circular Subarray [7, 6, 5, -4, -1, -1, 40] has the maximum sum, which is 52.
Constraints:
1 <= arr.size() <= 10^5
-104 <= arr[i] <= 10^4
"""
# Kadane's Algorithm


def maximumCircularSubarraySum(arr):
    totalSum = 0
    max_sum, min_sum = arr[0], arr[0]
    curr_max, curr_min = 0, 0
    for i in arr:
        totalSum += i

        curr_max = max(curr_max + i, i)
        max_sum = max(max_sum, curr_max)

        curr_min = min(curr_min + i, i)
        min_sum = min(min_sum, curr_min)

    if max_sum < 0:
        return max_sum
    max_circular_sum = totalSum - min_sum

    return max(max_sum, max_circular_sum)


arr = [8, -8, 9, -9, 10, -11, 12]
arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr1 = [-1, 40, -14, 7, 6, 5, -4, -1]
arr1 = [10, -3, -4, 7, 6, 5, -4, -1]
print(maximumCircularSubarraySum(arr))
