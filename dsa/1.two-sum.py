# def twoSum(nums, target):
#     seen = {}   # value : index

#     for i in range(len(nums)):
#         current = nums[i]
#         needed = target - current

#         if needed in seen:
#             return [seen[needed], i]

#         seen[current] = i


























def twosum(nums,target):
    seen={}

    for i in range(len(nums)):
        current=nums[i]
        needed=target-current

        if needed in seen:
            return (seen[needed],i)
        
        seen[current]=i

nums = [2, 7, 11, 15]
target = 9

result = twosum(nums, target)
print(result)