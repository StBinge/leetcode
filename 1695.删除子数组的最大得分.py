#
# @lc app=leetcode.cn id=1695 lang=python3
#
# [1695] 删除子数组的最大得分
#
from sbw import *
# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        include=set()
        left=0
        ret=0
        s=0
        for right,n in enumerate(nums):
            s+=n
            if n not in include:
                include.add(n)
                ret=max(ret,s)
            else:
                for i in range(left,right):
                    s-=nums[i]
                    include.remove(nums[i])
                    if nums[i]==n:
                        left=i+1
                        break
                include.add(n)
        return ret
# @lc code=end

assert Solution().maximumUniqueSubarray([5,2,1,2,5,2,1,2,5])==8
assert Solution().maximumUniqueSubarray([4,2,4,5,6])==17
