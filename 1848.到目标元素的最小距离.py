#
# @lc app=leetcode.cn id=1848 lang=python3
#
# [1848] 到目标元素的最小距离
#
from sbw import *


# @lc code=start
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        N = len(nums)
        ret = N
        for i in range(start,N):
            if nums[i]==target:
                ret=i-start
                break
        for j in range(start-1,max(start-ret-1,-1),-1):
            if nums[j]==target:
                ret=start-j
                break
        return ret

# @lc code=end
assert Solution().getMinDistance([5,3,6],5,2) == 2
assert Solution().getMinDistance(nums=[1, 2, 3, 4, 5], target=5, start=3) == 1
