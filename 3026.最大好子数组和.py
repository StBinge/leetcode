#
# @lc app=leetcode.cn id=3026 lang=python3
#
# [3026] 最大好子数组和
#
from sbw import *
# @lc code=start
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        min_s=defaultdict(lambda :float('inf'))
        ret=float('-inf')
        s=0
        for n in nums:
            min_s[n]=min(min_s[n],s)
            s+=n
            ret=max(ret,s-min(min_s[n-k],min_s[n+k]))
        return ret if ret>float('-inf') else 0

# @lc code=end
assert Solution().maximumSubarraySum([-9,0,-8,-7],1)==-15
assert Solution().maximumSubarraySum([3,4],2)==0
assert Solution().maximumSubarraySum(nums = [-1,-2,-3,-4], k = 2)==-6
assert Solution().maximumSubarraySum(nums = [-1,3,2,4,5], k = 3)==11
assert Solution().maximumSubarraySum(nums = [1,2,3,4,5,6], k = 1)==11
