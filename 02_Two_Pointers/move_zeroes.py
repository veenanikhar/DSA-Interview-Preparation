"""
Problem: Move Zeroes

Input:
arr = [0, 1, 0, 3, 12]

Output:
[1, 3, 12, 0, 0]

Pattern: Two Pointers - Same Direction

Approach:
1. Initialize i = 0.
2. Traverse the array using j.
3. If arr[j] is non-zero:
   - Swap arr[i] and arr[j].
   - Increment i.
4. Zeroes automatically move towards the end.

Time Complexity: O(N)
Space Complexity: O(1)
"""

arr = [0, 1, 0, 3, 12]
i = 0
for j in range(len(arr)):
    if arr[j] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1

print(arr)