#
# @lc app=leetcode.cn id=2643 lang=python3
# @lcpr version=30204
#
# [2643] 一最多的行
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row=mx_cnt=0
        for i,r in enumerate(mat):
            cnt=sum(r)
            if cnt>mx_cnt:
                mx_cnt=cnt
                row=i
        return [row,mx_cnt]
# @lc code=end



#
# @lcpr case=start
# [[0,1],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,0],[0,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0],[1,1],[0,0]]\n
# @lcpr case=end

#

