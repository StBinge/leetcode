#
# @lc app=leetcode.cn id=3238 lang=python3
# @lcpr version=30204
#
# [3238] 求出胜利玩家的数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        players=[[0]*11 for _ in range(n)]
        for p,b in pick:
            players[p][b]+=1
        return sum(any(b>i for b in players[i]) for i in range(n))
# @lc code=end



#
# @lcpr case=start
# 4\n[[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[1,1],[1,2],[1,3],[1,4]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[1,1],[2,4],[2,4],[2,4]]\n
# @lcpr case=end

#

