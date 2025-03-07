#
# @lc app=leetcode.cn id=3240 lang=python3
# @lcpr version=30204
#
# [3240] 最少翻转次数使二进制矩阵回文 II
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        ret=0
        for r in range(R//2):
            for c in range(C//2):
                cnt1=grid[r][c]+grid[-1-r][c]+grid[r][-1-c]+grid[-1-r][-1-c]
                ret+=min(cnt1,4-cnt1)
        
        cnt1=0
        modifer=0
        if R&1:
            row=grid[R//2]
            for c in range(C//2):
                _cnt1=row[c]+row[-1-c]
                if _cnt1==1:
                    modifer+=1
                else:
                    cnt1+=_cnt1
        if C&1:
            col=C//2
            for r in range(R//2):
                _cnt1=grid[r][col]+grid[-1-r][col]
                if _cnt1==1:
                    modifer+=1
                else:
                    cnt1+=_cnt1
        
        if R&1 and C&1:
            ret+=grid[R//2][C//2]
        
        return ret+(modifer if modifer>0 else cnt1%4)

                
        
# @lc code=end
assert Solution().minFlips( [[1],[1]])==2
assert Solution().minFlips([[1,1,1,1,1,0]])==1
assert Solution().minFlips([[1],[1],[1],[0]])==1
assert Solution().minFlips([[0,1],[0,1],[0,0]])==2
assert Solution().minFlips([[1,0,0],[0,1,0],[0,0,1]])==3


#
# @lcpr case=start
# [[1,0,0],[0,1,0],[0,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[0,1],[0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1],[1]]\n
# @lcpr case=end

#

