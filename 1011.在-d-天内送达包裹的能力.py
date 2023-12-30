#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#
from sbw import *
# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        while l<r:
            mid=(l+r)//2
            need=1
            cur=0
            for w in weights:
                if cur+w>mid:
                    need+=1
                    cur=0
                cur+=w
            if need<=days:
                r=mid
            else:
                l=mid+1
        return r

# @lc code=end
weights = [3,2,2,4,1,4]
days = 3
assert Solution().shipWithinDays(weights,days)==6

weights = [1,2,3,1,1]
days = 4
assert Solution().shipWithinDays(weights,days)==3

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
assert Solution().shipWithinDays(weights,days)==15
