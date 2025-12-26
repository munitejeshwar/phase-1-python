def twoSum(nums, target):
    seen = {}   # value : index

    for i in range(len(nums)):
        current = nums[i]
        needed = target - current

        if needed in seen:
            return [seen[needed], i]

        seen[current] = i
nums = [2, 7, 11, 15]
target = 9

result = twoSum(nums, target)
print(result)
