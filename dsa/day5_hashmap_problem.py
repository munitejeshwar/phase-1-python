def twosum(nums,target):
    seen={}
    for i in range(len(nums)):
        needed=target-nums[i]
        if needed in seen:
            return[seen[needed],i]
        seen[nums[i]]=i

nums=list(map(int,input().split()))
target=int(input())
print(twosum(nums,target))