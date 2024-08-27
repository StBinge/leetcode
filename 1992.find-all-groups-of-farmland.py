#
# @lc app=leetcode.cn id=1992 lang=python3
# @lcpr version=30204
#
# [1992] 找到所有的农场组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        R,C=len(land),len(land[0])
        ret=[]
        for r in range(R):
            for c in range(C):
                if land[r][c]==1 and (c==0 or land[r][c-1]==0) and (r==0 or land[r-1][c]==0):
                    r2=r+1
                    while r2<R and land[r2][c]==1:
                        r2+=1
                    r2-=1
                    c2=c+1
                    while c2<C and land[r][c2]==1:
                        c2+=1
                    c2-=1
                    ret.append([r,c,r2,c2])
        return ret
# @lc code=end
assert Solution().findFarmland( [[1,1],[1,1]])==[[0,0,1,1]]
assert Solution().findFarmland([[1,0,0],[0,1,1],[0,1,1]])==[[0,0,0,0],[1,1,2,2]]


#
# @lcpr case=start
# [[1,0,0],[0,1,1],[0,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0]]\n
# @lcpr case=end

#

