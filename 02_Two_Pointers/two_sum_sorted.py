
"""
Problem: Two Sum II - Sorted Array

Input:
arr = [1, 2, 4, 6, 8, 9]
target = 12

Output:
[4, 8]

Pattern: Two Pointers - Opposite Direction

Approach:
1. Initialize left at the first index.
2. Initialize right at the last index.
3. Calculate the sum of both elements.
4. If sum equals target, return the pair.
5. If sum is smaller than target, move left forward.
6. If sum is greater than target, move right backward.
7. If no pair is found, return an empty list.

Time Complexity: O(N)
Space Complexity: O(1)
"""

def two_sum(arr, target):
    left = 0 
    right = len(arr) - 1

    while left < right:

        total = arr[left] + arr[right]

        if total == target:
            return [arr[left], arr[right]]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []

arr = [1, 2, 4, 6, 8, 9]
target = 12

print(two_sum(arr, target))
