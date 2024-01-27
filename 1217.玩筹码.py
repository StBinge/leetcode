#
# @lc app=leetcode.cn id=1217 lang=python3
#
# [1217] 玩筹码
#
from sbw import *
# @lc code=start
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        cnt=[0,0]
        for pos in position:
            cnt[pos%2]+=1
        return min(cnt)
# @lc code=end
assert Solution().minCostToMoveChips([1,1000000000])==1
assert Solution().minCostToMoveChips([2,2,2,3,3])==2
assert Solution().minCostToMoveChips([1,2,3])==1
