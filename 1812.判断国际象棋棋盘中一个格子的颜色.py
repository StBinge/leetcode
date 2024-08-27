#
# @lc app=leetcode.cn id=1812 lang=python3
#
# [1812] 判断国际象棋棋盘中一个格子的颜色
#


# @lc code=start
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        row = ord(coordinates[1]) - ord("1")
        col = ord(coordinates[0]) - ord("a")
        # return (row & 1 != col & 1==1) or (row &1==col&1==0)
        return (row + col) % 2 == 1


# @lc code=end

assert Solution().squareIsWhite("c7") == False
assert Solution().squareIsWhite("h3")
assert Solution().squareIsWhite("a1") == False
