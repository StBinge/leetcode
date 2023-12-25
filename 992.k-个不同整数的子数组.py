#
# @lc app=leetcode.cn id=992 lang=python3
#
# [992] K 个不同整数的子数组
#
from sbw import *


# @lc code=start
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        Max=max(nums)
        L = len(nums)

        def atMost(k):
            nonlocal Max,L
            freq=[0]*(Max+1)
            cnt=0
            ret=0
            l=r=0
            while r<L:
                if freq[nums[r]]==0:
                    cnt+=1
                freq[nums[r]]+=1
                r+=1
                while cnt>k:
                    freq[nums[l]]-=1
                    if freq[nums[l]]==0:
                        cnt-=1
                    l+=1
                ret+=r-l
            return ret
        return atMost(k)-atMost(k-1)

# @lc code=end
nums = [1, 2, 1, 2, 3]
k = 2
assert Solution().subarraysWithKDistinct(nums, k) == 7
