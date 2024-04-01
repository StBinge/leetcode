#
# @lc app=leetcode.cn id=1493 lang=python3
#
# [1493] 删掉一个元素以后全为 1 的最长子数组
#
from sbw import *
# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ret=f0=f1=0
        for n in nums:
            if n==1:
                f0+=1
                f1+=1
            else:
                f0,f1=0,f0
            ret=max(ret,f1)
        return min(ret,len(nums)-1)
 
# @lc code=end
assert Solution().longestSubarray([1,1,1])==2
assert Solution().longestSubarray([1,1,0,1])==3
assert Solution().longestSubarray([0,1,1,1,0,1,1,0,1])==5
