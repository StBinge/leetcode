#
# @lc app=leetcode.cn id=2673 lang=python3
# @lcpr version=30204
#
# [2673] 使二叉树所有路径值相等的最小代价
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ret=0
        for i in range(n//2,0,-1):
            ret+=abs(cost[i*2-1]-cost[i*2])
            cost[i-1]+=max(cost[i*2-1],cost[i*2])
        return ret
# @lc code=end
assert Solution().minIncrements(n = 3, cost = [5,3,3])==0
assert Solution().minIncrements(n = 7, cost = [1,5,2,2,3,3,1])==6


#
# @lcpr case=start
# 7\n[1,5,2,2,3,3,1]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[5,3,3]\n
# @lcpr case=end

#

