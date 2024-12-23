#
# @lc app=leetcode.cn id=2661 lang=python3
# @lcpr version=30204
#
# [2661] 找出叠涂元素
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        R,C=len(mat),len(mat[0])
        pos_map={}
        for r in range(R):
            for c in range(C):
                pos_map[mat[r][c]]=[r,c]
        
        rows=[0]*R
        cols=[0]*C
        for i,n in enumerate(arr):
            r,c=pos_map[n]
            rows[r]+=1
            cols[c]+=1
            if rows[r]==C or cols[c]==R:
                return i
        
# @lc code=end



#
# @lcpr case=start
# [1,3,4,2]\n[[1,4],[2,3]]\n
# @lcpr case=end

# @lcpr case=start
# [2,8,7,4,1,3,5,6,9]\n[[3,2,5],[1,4,6],[8,7,9]]\n
# @lcpr case=end

#

