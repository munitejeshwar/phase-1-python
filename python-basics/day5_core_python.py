# text=input()
# def frequency_counter(text):
#     count={}
#     for ch in text:
#         if ch in count:
#             count[ch]+=1;
#         else:
#             count[ch]=1
#     return count
# print(frequency_counter(text))


# nums=list(map(int, input().split()))
# def rem_dup(nums):
#     result = []

#     for n in nums:
#         if n not in result:
#             result.append(n)
#     return(result)
# print(rem_dup(nums))




text=input()
v={"a","e","i","o","u"}
def vow_count(text):
    count=0
    for ch in text:
        if ch in v:
            count+=1
    return(count)
print(vow_count(text))
