#
# @lc app=leetcode.cn id=1802 lang=python3
#
# [1802] 有界数组中指定下标处的最大值
#
from sbw import *
# @lc code=start
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        L=index
        R=n-1-L
        if L>R:
            L,R=R,L

        big=math.floor(math.sqrt(maxSum-n+17/4)+5/2)
        if big<=L+1:
            return big
        
        big=math.floor(math.sqrt(2*(maxSum-R-1)+L*L+L+(2*L+1)**2/4)-(2*L-1)/2)
        if L+1<=big<=R+1:
            return big
        
        big=math.floor((2*maxSum+n+L*L+R*R)/2*(n+1))
        return big


# @lc code=end
assert Solution().maxValue( n = 6, index = 1,  maxSum = 10)==3
assert Solution().maxValue( 3,2,18)==7
assert Solution().maxValue( 9,3,16)==3
assert Solution().maxValue( n= 4, index = 2,  maxSum = 6)==2
