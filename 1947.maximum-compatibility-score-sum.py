#
# @lc app=leetcode.cn id=1947 lang=python3
# @lcpr version=30204
#
# [1947] 最大兼容性评分和
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        M=len(students)
        N=len(students[0])
        for i in range(M):
            mask=0
            for d in students[i]:
                mask=(mask<<1)+d
            students[i]=mask
            mask=0
            for d in mentors[i]:
                mask=(mask<<1)+d
            mentors[i]=mask
        Mask=1<<M
        f=[float('inf')]*Mask
        f[0]=0
        for mask in range(1,Mask):
            bits=mask.bit_count()
            for i in range(M):
                if mask & 1<<i:
                    f[mask]=min(f[mask^(1<<i)]+(students[bits-1]^mentors[i]).bit_count(),f[mask])
        return M*N-f[-1]
# @lc code=end
assert Solution().maxCompatibilitySum(students = [[0,0],[0,0],[0,0]], mentors = [[1,1],[1,1],[1,1]])==0
assert Solution().maxCompatibilitySum(students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]])==8


#
# @lcpr case=start
# [[1,1,0],[1,0,1],[0,0,1]]\n[[1,0,0],[0,0,1],[1,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0],[0,0],[0,0]]\n[[1,1],[1,1],[1,1]]\n
# @lcpr case=end

#

