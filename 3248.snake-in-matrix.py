#
# @lc app=leetcode.cn id=3248 lang=python3
# @lcpr version=30204
#
# [3248] 矩阵中的蛇
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        r=c=0
        for dir in commands:
            if dir=='LEFT':
                c-=1
            elif dir=='RIGHT':
                c+=1
            elif dir=='UP':
                r-=1
            else:
                r+=1
        return r*n+c
# @lc code=end



#
# @lcpr case=start
# 2\n["RIGHT","DOWN"]\n
# @lcpr case=end

# @lcpr case=start
# 3\n["DOWN","RIGHT","UP"]\n
# @lcpr case=end

#

