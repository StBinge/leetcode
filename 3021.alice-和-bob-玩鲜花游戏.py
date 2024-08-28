#
# @lc app=leetcode.cn id=3021 lang=python3
#
# [3021] Alice 和 Bob 玩鲜花游戏
#


# @lc code=start
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return n*m//2


# @lc code=end
assert Solution().flowerGame(1, 1) == 0
assert Solution().flowerGame(3, 2) == 3
