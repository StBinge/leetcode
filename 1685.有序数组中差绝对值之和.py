#
# @lc app=leetcode.cn id=1685 lang=python3
#
# [1685] 有序数组中差绝对值之和
#
from sbw import *
# @lc code=start
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        ret=[0]*len(nums)
        tot=sum(nums)
        cur=0
        N=len(nums)
        for i,n in enumerate(nums):
            ret[i]=i*n-cur+(tot-cur)-(N-i)*n
            cur+=n
        return ret

# @lc code=end
assert Solution().getSumAbsoluteDifferences([2,3,5])==[4,3,5]
assert Solution().getSumAbsoluteDifferences([1,4,6,8,10])==[24,15,13,15,21]
