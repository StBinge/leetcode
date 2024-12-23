#
# @lc app=leetcode.cn id=LCR 088 lang=python3
# @lcpr version=30204
#
# [LCR 088] 使用最小花费爬楼梯
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f0=f1=0
        N=len(cost)
        for i in range(2,N+1):
            f0,f1=f1,min(f0+cost[i-2],f1+cost[i-1])
        return f1
# @lc code=end
assert Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])==6
assert Solution().minCostClimbingStairs([10,15,20])==15


#
# @lcpr case=start
# [10, 15, 20]\n
# @lcpr case=end

# @lcpr case=start
# [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]\n
# @lcpr case=end

#

