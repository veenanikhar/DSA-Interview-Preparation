
"""
Problem: Reverse an Array

Input:
arr = [5, 10, 15, 20, 25, 30]

Output:
[30, 25, 20, 15, 10, 5]

Pattern: Two Pointers - Opposite Direction

Approach:
1. Initialize left at the first index.
2. Initialize right at the last index.
3. Swap the elements at left and right.
4. Move left forward and right backward.
5. Continue until left is no longer less than right.

Time Complexity: O(N)
Space Complexity: O(1)
"""

arr = [5, 10, 15, 20, 25, 30]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]

    left += 1
    right -= 1

print(arr)