#
# @lc app=leetcode.cn id=1330 lang=python3
#
# [1330] 翻转子数组得到最大的数组值
#
from sbw import *
# @lc code=start
class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        ret=0
        mi,ma=float('inf'),float('-inf')
        a=nums[0]
        d=0
        for b in nums[1:]:
            mi=min(mi,max(b,a))
            ma=max(ma,min(b,a))
            dif=abs(a-b)
            d=max(d,abs(nums[0]-b)-dif,
                  abs(nums[-1]-a)-dif)
            ret+=dif
            a=b
        return ret+max(d,2*(ma-mi))

# @lc code=end
assert Solution().maxValueAfterReverse([2,4,9,24,2,1,10])==68
assert Solution().maxValueAfterReverse(nums = [2,3,1,5,4])==10
