#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#
from sbw import *
# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        return sum(v*(v-1)//2 for v in cnt.values())
# @lc code=end
assert Solution().numIdenticalPairs([1,2,3,1,1,3])==4
