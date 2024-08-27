#
# @lc app=leetcode.cn id=2132 lang=python3
# @lcpr version=30204
#
# [2132] 用邮票贴满网格图
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        R,C=len(grid),len(grid[0])
        



# @lc code=end
assert Solution().possibleToStamp([[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,1],[0,0,0,1,1]],2,2)==False
assert Solution().possibleToStamp([[0],[0],[0],[0],[0],[0]],6,1)


#
# @lcpr case=start
# [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]\n4\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]\n2\n2\n
# @lcpr case=end

#

