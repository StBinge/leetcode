#
# @lc app=leetcode.cn id=3360 lang=python3
# @lcpr version=30204
#
# [3360] 移除石头游戏
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn = 0
        stone = 10
        while n >= stone:
            n -= stone
            turn ^= 1
            stone -= 1
        return turn != 0


# @lc code=end


#
# @lcpr case=start
# 12\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#
