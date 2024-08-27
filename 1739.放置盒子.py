#
# @lc app=leetcode.cn id=1739 lang=python3
#
# [1739] 放置盒子
#
from sbw import *
# @lc code=start
class Solution:
    def minimumBoxes(self, n: int) -> int:
        x=int((6*n)**(1/3))
        if x*(x+1)*(x+2)//6>n:
            x-=1
        N=n-x*(x+1)*(x+2)//6
        return x*(x+1)//2+math.ceil((-1+(1+8*N)**0.5)/2)
        
# @lc code=end
assert Solution().minimumBoxes(10)==6
assert Solution().minimumBoxes(4)==3
assert Solution().minimumBoxes(3)==3
