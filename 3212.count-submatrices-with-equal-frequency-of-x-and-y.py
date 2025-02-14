#
# @lc app=leetcode.cn id=3212 lang=python3
# @lcpr version=30204
#
# [3212] 统计 X 和 Y 频数相等的子矩阵数量
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        R,C=len(grid),len(grid[0])
        ret=0
        cols_cnt=[[0,0] for _ in range(C)]
        x=y=0
        for row in grid:
            x=y=0
            for c in range(C):
                if row[c]!='.':
                    cols_cnt[c][ord(row[c])&1]+=1
                x+=cols_cnt[c][0]
                y+=cols_cnt[c][1]
                if x>0 and x==y:
                    ret+=1
        return ret
# @lc code=end



#
# @lcpr case=start
# [["X","Y","."],["Y",".","."]]\n
# @lcpr case=end

# @lcpr case=start
# [["X","X"],["X","Y"]]\n
# @lcpr case=end

# @lcpr case=start
# [[".","."],[".","."]]\n
# @lcpr case=end

#

