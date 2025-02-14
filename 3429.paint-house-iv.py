#
# @lc app=leetcode.cn id=3429 lang=python3
# @lcpr version=30204
#
# [3429] 粉刷房子 IV
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        codes=[12,13,21,23,31,32]
        valid_match=[
            [21,23,31],
            [21,31,32],
            [12,13,32],
            [12,31,32],
            [12,13,23],
            [13,21,23]
        ]
        f=[0]*6

        for i in range(n//2):
            _f=[float('inf')]*6
            for j in range(6):
                for nxt in valid_match[j]:
                    code=codes.index(nxt)
                    l,r=divmod(nxt,10)
                    _f[code]=min(_f[code],f[j]+cost[i][l-1]+cost[n-i-1][r-1])
            f=_f
        return min(f)
# @lc code=end
assert Solution().minCost(n = 4, cost = [[3,5,7],[6,2,9],[4,8,1],[7,3,5]])==9


#
# @lcpr case=start
# 4\n[[3,5,7],[6,2,9],[4,8,1],[7,3,5]]\n
# @lcpr case=end

# @lcpr case=start
# 6\n[[2,4,6],[5,3,8],[7,1,9],[4,6,2],[3,5,7],[8,2,4]]\n
# @lcpr case=end

#

