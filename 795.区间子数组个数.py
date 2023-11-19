#
# @lc app=leetcode.cn id=795 lang=python3
#
# [795] 区间子数组个数
#
from typing import List
# @lc code=start
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound):
            cur=ret=0
            for n in nums:
                if n<=bound:
                    cur+=1
                    ret+=cur
                else:
                    cur=0
            return ret
        return count(right)-count(left-1)
# @lc code=end
nums=[73,55,36,5,55,14,9,7,72,52]
left=32
right=69
assert Solution().numSubarrayBoundedMax(nums,left,right)==22

nums = [2,1,4,3]
left = 2
right = 3
assert Solution().numSubarrayBoundedMax(nums,left,right)==3

nums = [2,9,2,5,6]
left = 2
right = 8
assert Solution().numSubarrayBoundedMax(nums,left,right)==7