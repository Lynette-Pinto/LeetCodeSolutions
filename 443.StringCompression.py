from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        print(chars)
        n=len(chars)-1
        count=1
        read=0
        write=0

        while read < n:
            if chars[read]==chars[read+1]:
                count +=1
            else:
                if count>1:
                    
                    chars[write]=chars[read] 
                    write +=1
                    chars[write]=count
                    write +=1
                    count=1
                else:
                    
                    write+=1
            read +=1
        if count>1:
            
            chars[write]=chars[read] 
            write +=1
            chars[write]=count
            write +=1

        else:
           
            write +=1
            chars[write]=chars[read]
        chars2=chars[:write+1]
        chars.clear()
        chars=chars2
        print(chars)


        
        # for i in range(n):
        #     if chars[i] not in chars[n:]:
        #         chars.append(chars[i])
        #         count=chars.count(chars[i])-1
        #         if count > 9:
        #             for d in str(count):
        #                 chars.append(d)
        #         elif count > 1:
        #             chars.append(str(count))
        #     else:
        #         continue
        # chars=chars[n:]

        # return len(chars)

            
                

            
chars = ["a","a","a","b","b","a","a"]
sol = Solution()
print(sol.compress(chars))   
