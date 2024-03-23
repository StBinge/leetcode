#
# @lc app=leetcode.cn id=1362 lang=python3
#
# [1362] 最接近的因数
#
from sbw import *
# @lc code=start
import math
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def get_factors(n):
            f=int(math.sqrt(n))
            for i in range(f,0,-1):
                if n%i==0:
                    return [i,n//i]
        ff1=get_factors(num+1)
        dis1=abs(ff1[0]-ff1[1])
        ff2=get_factors(num+2)
        dis2=abs(ff2[0]-ff2[1])
        return ff1 if dis1<dis2 else ff2
# @lc code=end
assert sorted(Solution().closestDivisors(999))==sorted([40,25])
assert sorted(Solution().closestDivisors(123))==sorted([5,25])
assert sorted(Solution().closestDivisors(8))==sorted([3,3])
