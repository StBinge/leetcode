#
# @lc app=leetcode.cn id=2830 lang=python3
# @lcpr version=30204
#
# [2830] 销售利润最大化
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        ends=[[] for _ in range(n)]
        for x,y,g in offers:
            ends[y].append([x,g])
        
        f=[0]*(n+1)
        for i in range(1,n+1):
            f[i]=f[i-1]
            for s,g in ends[i-1]:
                f[i]=max(f[i],f[s]+g)
        return max(f)
# @lc code=end

assert Solution().maximizeTheProfit(4,[[0,0,6],[1,2,8],[0,3,7],[2,2,5],[0,1,5],[2,3,2],[0,2,8],[2,3,10],[0,3,2]])==16
assert Solution().maximizeTheProfit(4,[[1,3,10],[1,3,3],[0,0,1],[0,0,7]])==17
assert Solution().maximizeTheProfit(n = 5, offers = [[0,0,1],[0,2,10],[1,3,2]])==10
assert Solution().maximizeTheProfit(n = 5, offers = [[0,0,1],[0,2,2],[1,3,2]])==3

#
# @lcpr case=start
# 5\n[[0,0,1],[0,2,2],[1,3,2]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[0,0,1],[0,2,10],[1,3,2]]\n
# @lcpr case=end

#

