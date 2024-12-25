#
# @lc app=leetcode.cn id=3127 lang=python3
# @lcpr version=30204
#
# [3127] 构造相同颜色的正方形
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for r in range(2):
            for c in range(2):
                b=0
                for i in range(2):
                    for j in range(2):
                        if grid[r+i][c+j]=='B':
                            b+=1
                if b!=2:
                    return True
        return False
                    



# @lc code=end



#
# @lcpr case=start
# [["B","W","B"],["B","W","W"],["B","W","B"]]\n
# @lcpr case=end

# @lcpr case=start
# [["B","W","B"],["W","B","W"],["B","W","B"]]\n
# @lcpr case=end

# @lcpr case=start
# [["B","W","B"],["B","W","W"],["B","W","W"]]\n
# @lcpr case=end

#

