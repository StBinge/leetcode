#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#
from typing import List
# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cur=pre=0
        for i in range(2,len(cost)+1):
            pre,cur=cur,min(pre+cost[i-2],cur+cost[i-1])
        return cur
# @lc code=end
cost=[1,100,1,1,1,100,1,1,100,1]
assert Solution().minCostClimbingStairs(cost)==6
cost = [10,15,20]
assert Solution().minCostClimbingStairs(cost)==15
