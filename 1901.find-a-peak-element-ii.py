#
# @lc app=leetcode.cn id=1901 lang=python3
# @lcpr version=30204
#
# [1901] 寻找峰值 II
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        R,C=len(mat),len(mat[0])
        left,right=0,R-2
        def find_mx_id(row):
            ret=0
            for i in range(1,C):
                if row[i]>row[ret]:
                    ret=i
            return ret
        
        while left<=right:
            mid=(left+right)//2
            idx=find_mx_id(mat[mid])
            if mat[mid+1][idx]>mat[mid][idx]:
                left=mid+1
            elif mat[mid+1][idx]<mat[mid][idx]:
                right=mid-1
        return [left,find_mx_id(mat[left])]
# @lc code=end
assert Solution().findPeakGrid([[10,20,15],[21,30,14],[7,16,32]])==[1,1]
assert Solution().findPeakGrid([[1,4],[3,2]])==[0,1]


#
# @lcpr case=start
# [[1,4],[3,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[10,20,15],[21,30,14],[7,16,32]]\n
# @lcpr case=end

#

