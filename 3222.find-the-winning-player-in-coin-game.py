#
# @lc app=leetcode.cn id=3222 lang=python3
# @lcpr version=30204
#
# [3222] 求出硬币游戏的赢家
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        round=min(x,y//4)
        return 'Alice' if round&1 else 'Bob'
# @lc code=end



#
# @lcpr case=start
# 2\n7\n
# @lcpr case=end

# @lcpr case=start
# 4\n11\n
# @lcpr case=end

#

