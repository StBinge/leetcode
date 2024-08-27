#
# @lc app=leetcode.cn id=1578 lang=python3
#
# [1578] 使绳子变成彩色的最短时间
#
from sbw import *


# @lc code=start
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        pre=colors[0]
        ret=0
        max_cost=neededTime[0]
        tot_cost=neededTime[0]
        repeated=False
        for i in range(1,len(colors)):
            if colors[i]!=pre:
                if repeated:
                    ret+=tot_cost-max_cost
                    repeated=False
                pre=colors[i]
                max_cost=neededTime[i]
                tot_cost=max_cost
            else:
                repeated=True
                max_cost=max(max_cost,neededTime[i])
                tot_cost+=neededTime[i]
        if repeated:
            ret+=tot_cost-max_cost
        return ret
# @lc code=end
assert Solution().minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1]) == 2
assert Solution().minCost(colors="abc", neededTime=[1, 2, 3]) == 0
assert Solution().minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5]) == 3
