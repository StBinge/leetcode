#
# @lc app=leetcode.cn id=788 lang=python3
#
# [788] 旋转数字
#

# @lc code=start
from functools import lru_cache
class Solution:
    def rotatedDigits(self, n: int) -> int:
        flags=[0,0,1,-1,-1,1,1,-1,0,1]
        
        digits=[int(d) for d in str(n)]

        @lru_cache
        def counter(pos,bound,diff):
            if pos==len(digits):
                return int(diff)
            
            ret=0
            for i in range(0,(9 if not bound else digits[pos])+1):
                if flags[i]==-1:
                    continue
                ret+=counter(
                    pos+1,
                    bound and i==digits[pos],
                    diff or flags[i]==1
                )
            return ret
        
        return counter(0,True,False)



# @lc code=end

assert Solution().rotatedDigits(857)==247
assert Solution().rotatedDigits(10)==4
assert Solution().rotatedDigits(2)==1