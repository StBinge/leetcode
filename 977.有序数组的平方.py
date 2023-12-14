#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#
from sbw import *
# @lc code=start
import bisect
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        L=len(nums)
        ret=[0]*L
        idx=L-1
        i,j=0,L-1
        while i<=j:
            if abs(nums[i])<abs(nums[j]):
                ret[idx]=nums[j]**2
                j-=1
            else:
                ret[idx]=nums[i]**2
                i+=1
            idx-=1
        return ret

        
# @lc code=end
nums = [-7,-3,2,3,11]
ret=[4,9,9,49,121]
assert Solution().sortedSquares(nums)==ret

nums = [-4,-1,0,3,10]
ret=[0,1,9,16,100]
assert Solution().sortedSquares(nums)==ret
