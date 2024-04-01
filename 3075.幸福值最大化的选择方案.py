#
# @lc app=leetcode.cn id=3075 lang=python3
#
# [3075] 幸福值最大化的选择方案
#
from sbw import *
# @lc code=start
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ret=0
        minus=0
        for h in happiness[:k]:
            if h<=minus:
                break
            ret+=h-minus
            minus+=1
        return ret
# @lc code=end
assert Solution().maximumHappinessSum([12,1,42],3)==53
assert Solution().maximumHappinessSum(happiness = [2,3,4,5], k = 1)==5
assert Solution().maximumHappinessSum(happiness = [1,1,1,1], k = 2)==1
assert Solution().maximumHappinessSum(happiness = [1,2,3], k = 2)==4
