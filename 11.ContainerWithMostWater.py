class Solution:
    def maxArea(self, height: list[int]) -> int:
        start = 0
        max_area=0
        end = len(height)-1
        print(height)      
        while start<=end:
            min_h=min(height[start], height[end])
            
            area= min_h*(end-start)
            if(area > max_area):
                max_area=area
            if height[start] <= height[end]:
                start+=1
            else:
                end=end-1
        print(start)
        print(end)
        print(max_area)
height=[1,1]

sol = Solution()
print(sol.maxArea(height))