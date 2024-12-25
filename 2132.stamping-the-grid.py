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

        size=stampHeight*stampWidth
        R,C=len(grid),len(grid[0])
        tot=R*C
        pre_matrix=[[0]*(C+1) for _ in range(R+1)]
        for r in range(R):
            for c in range(C):
                pre_matrix[r+1][c+1]=pre_matrix[r][c+1]+pre_matrix[r+1][c]+grid[r][c]-pre_matrix[r][c]
        
        covered=set()
        for r in range(r-1,R):
            for c in range(C):
                if grid[r][c]:
                    tot-=1
                    continue
                if pre_matrix[r+1][c+1]-

        



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

