
from typing import List

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start=0
        for ch in t:
            if start<len(s):
                if ch==s[start]:
                    start+=1
        
        return (start==len(s))
                

     


s="abc"
t="ahbgdc"

sol = Solution()
print(sol.isSubsequence(s,t))
