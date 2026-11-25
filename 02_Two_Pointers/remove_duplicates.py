
"""
Problem: Remove Duplicates from Sorted Array

Input:
arr = [1, 1, 2, 2, 3, 4, 4, 5]

Output:
Unique Count: 5
Unique Elements: [1, 2, 3, 4, 5]

Pattern: Two Pointers - Same Direction

Approach:
1. If the array is empty, return 0.
2. Initialize slow pointer i = 0.
3. Start fast pointer j from index 1.
4. Compare arr[i] with arr[j].
5. If both are equal, move j forward.
6. If they are different:
   - Move i forward.
   - Copy arr[j] into arr[i].
7. Return i + 1, which represents the number of unique elements.

Time Complexity: O(N)
Space Complexity: O(1)
"""

def remove_duplicates(arr):
    if not arr:
        return 0

    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1

arr = [1, 1, 2, 2, 3, 4, 4, 5]

r = remove_duplicates(arr)

print("Unique Count:", r)
print("Unique Elements:", arr[:r])
    



