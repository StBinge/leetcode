#
# @lc app=leetcode.cn id=1975 lang=python3
# @lcpr version=30204
#
# [1975] 最大方阵和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        mi=float('inf')
        negs=0
        s=0
        for row in matrix:
            for cell in row:
                mi=min(mi,abs(cell))
                if cell<0:
                    negs+=1
                    s-=cell
                else:
                    s+=cell
        if negs&1:
            return s-2*mi
        else:
            return s
# @lc code=end
assert Solution().maxMatrixSum([[2,9,3],[5,4,-4],[1,7,1]])==34
assert Solution().maxMatrixSum([[-1,0,-1],[-2,1,3],[3,2,2]])==15
assert Solution().maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]])==16
assert Solution().maxMatrixSum([[1,-1],[-1,1]])==4


#
# @lcpr case=start
# [[1,-1],[-1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[-1,-2,-3],[1,2,3]]\n
# @lcpr case=end

#

