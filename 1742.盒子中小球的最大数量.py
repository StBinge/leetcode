#
# @lc app=leetcode.cn id=1742 lang=python3
#
# [1742] 盒子中小球的最大数量
#
from sbw import *
# @lc code=start
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        cnt=[0]*50
        def max_range(x):
            return min(x//10*10+9,highLimit)
        
        def index(x):
            ret=0
            while x:
                ret+=x%10
                x//=10
            return ret

        while lowLimit<=highLimit:
            l,r=lowLimit,max_range(lowLimit)
            cnt[index(l)]+=1
            cnt[index(r)+1]-=1
            lowLimit=r+1
        
        cur=0
        ret=0
        for c in cnt:
            cur+=c
            ret=max(ret,cur)
        return ret
# @lc code=end
assert Solution().countBalls(lowLimit = 1, highLimit = 10)==2
assert Solution().countBalls(lowLimit = 5, highLimit = 15)==2
