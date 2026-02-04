"""
Approach:
- Use a set to store seen elements
- While traversing the array, check if element already exists in set
- If yes, duplicate found
- If not, add element to set

Time Complexity:
- O(n)

Space Complexity:
- O(n)
"""

def contains_duplicate(nums):
    seen = set()

    for n in nums:
        if n in seen:
            return True
        seen.add(n)

    return False


print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))
