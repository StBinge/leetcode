#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#
from sbw import *
# @lc code=start
import bisect
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,rsum,lsum=0,0,0
        L=len(nums)
        ret=0
        for right in range(L):
            rsum+=1-nums[right]
            while rsum-lsum>k:
                lsum+=1-nums[left]
                left+=1
            ret=max(ret,right-left+1)
        return ret

# @lc code=end
nums = [0,0,0,1]
K = 4
# assert Solution().longestOnes(nums,K)==4

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3
assert Solution().longestOnes(nums,K)==10

nums = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
assert Solution().longestOnes(nums,K)==6
