#
# @lc app=leetcode.cn id=1675 lang=python3
#
# [1675] 数组的最小偏移量
#
from sbw import *


# @lc code=start
from sortedcontainers import SortedList
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        p_max=1
        for n in nums:
            while n&1==0:
                n>>=1
            p_max=max(p_max,n)
        
        upper=[]
        mi=p_max
        for n in nums:
            if n&1:
                n<<=1
            while n>=2*p_max:
                n>>=1
            if n>=p_max:
                upper.append(n)
            mi=min(mi,n)
        upper.sort()
        ret=upper[-1]-mi
        for i in range(len(upper)-1,0,-1):
            if upper[i]<=p_max:
                break
            mi=min(mi,upper[i]//2)
            ret=min(ret,upper[i-1]-mi)
        return ret


# @lc code=end
assert Solution().minimumDeviation([10,4,3]) == 2
assert Solution().minimumDeviation([3, 5]) == 1
assert Solution().minimumDeviation([2, 10, 8]) == 3
assert Solution().minimumDeviation([4, 1, 5, 20, 3]) == 3
assert Solution().minimumDeviation([1, 2, 3, 4]) == 1
