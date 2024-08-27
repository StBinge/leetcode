#
# @lc app=leetcode.cn id=1823 lang=python3
#
# [1823] 找出游戏的获胜者
#

from sbw import *
# @lc code=start
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        idx=0
        for i in range(2,n+1):
            idx=(idx+k)%i
        return idx+1
        


# @lc code=end
assert Solution().findTheWinner(5, 4) == 1
assert Solution().findTheWinner(n=6, k=5) == 1
assert Solution().findTheWinner(n=5, k=2) == 3
