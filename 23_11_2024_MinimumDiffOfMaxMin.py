"""
Given a positive integer k and an array arr[] denoting heights of towers,
you have to modify the height of each tower either by increasing or decreasing them by k only once.
Find out what could be the possible minimum difference of the height of
shortest and longest towers after you have modified each tower.

Note: A slight modification of the problem can be found here.

Examples:

Input: k = 2, arr[] = [1, 5, 8, 10]
Output: 5
Explanation: The array can be modified as [3, 3, 6, 8]. The difference between the largest and the smallest is 8 - 3 = 5.
Input: k = 3, arr[] = [3, 9, 12, 16, 20]
Output: 11
Explanation: The array can be modified as [6, 12, 9, 13, 17]. The difference between the largest and the smallest is 17 - 6 = 11.
Constraints
1 ≤ k ≤ 10^4
1 ≤ number of towers ≤ 10^5
0 ≤ arr[i] ≤ 10^5
"""


def minMaxDiff(arr, k):
    arr.sort()
    n = len(arr)

    # Initialize the answer with the current max difference
    ans = arr[-1] - arr[0]

    # Traverse the array and calculate the possible minimum differences
    for i in range(1, n):
        min_height = min(arr[0] + k, arr[i] - k)
        max_height = max(arr[i - 1] + k, arr[-1] - k)

        ans = min(ans, max_height - min_height)

    return ans


arr1 = [3, 9, 12, 16, 20]
arr = [-10, -2, -8, 2, 3]
k = 4
print(minMaxDiff(arr, k))