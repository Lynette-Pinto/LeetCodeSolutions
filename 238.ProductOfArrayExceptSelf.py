import math
nums = [-1,1,0,-3,3]
prod=1
n=len(nums)
res=[]
total_prod = math.prod(nums)
if total_prod !=0:
    for i in range(n):
        res.append(total_prod//nums[i])
    #return res
    print(res)
elif total_prod==1:
    #return nums
    print(nums)
else:
    for i in range(n):
        res.append(math.prod(nums[:i]+ nums[i+1:]))
    #return res
    print(res)
#if 0 not in nums:
#     total_prod = math.prod(nums)
#     result = [total_prod // x for x in nums]
#     print(result)
# else:
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             prod=prod*nums[i]
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             result = [prod if j == i else 0 for j in range(len(nums))]
#             break
#     print(result)