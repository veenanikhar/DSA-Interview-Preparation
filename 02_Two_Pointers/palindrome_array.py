
"""
Problem: Check if an Array is Palindrome

Input:
arr = [1, 2, 3, 2, 1]

Output:
True

Pattern: Two Pointers - Opposite Direction

Approach:
1. Initialize left at the first index.
2. Initialize right at the last index.
3. Compare elements at both pointers.
4. If they are different, return False.
5. If they match, move left forward and right backward.
6. If all pairs match, return True.

Time Complexity: O(N)
Space Complexity: O(1)
"""

def is_palindrome(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True

arr = [1, 2, 3, 2, 1]

print(is_palindrome(arr))
