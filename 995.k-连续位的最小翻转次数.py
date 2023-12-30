#
# @lc app=leetcode.cn id=995 lang=python3
#
# [995] K 连续位的最小翻转次数
#
from sbw import *
# @lc code=start
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        L=len(nums)

        rev_cnt=0
        ret=0
        for i,n in enumerate(nums):
            if i>=k and nums[i-k]>1:
                rev_cnt^=1
            if rev_cnt==n:
                if i+k>L:
                    return -1
                ret+=1
                rev_cnt^=1
                nums[i]+=2
        return ret 
        
# @lc code=end
nums = [0,0,0,1,0,1,1,0]
K = 3
assert Solution().minKBitFlips(nums,K)==3

nums = [1,1,0]
K = 2
assert Solution().minKBitFlips(nums,K)==-1

nums = [0,1,0]
K = 1
assert Solution().minKBitFlips(nums,K)==2
