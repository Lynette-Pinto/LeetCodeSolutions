from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=0
        for x in nums:
            if x!= 0:
                nums[n]=x
                n+=1
        
        nums[n:]=[0]* (len(nums)- n)
        print(nums)

nums = [0,1,1,0,0]

sol = Solution()
print(sol.moveZeroes(nums))   
