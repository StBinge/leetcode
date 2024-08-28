#
# @lc app=leetcode.cn id=1838 lang=python3
#
# [1838] 最高频元素的频数
#
from sbw import *
# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        N=len(nums)
        left=0
        ret=1
        for right in range(1,N):
            dif=nums[right]-nums[right-1]
            k-=dif*(right-left)
            while k<0:
                k+=nums[right]-nums[left]
                left+=1
            ret=max(ret,right-left+1)
        return ret

# @lc code=end
assert Solution().maxFrequency([100000],100000)==1
assert Solution().maxFrequency(nums = [3,9,6], k = 2)==1
assert Solution().maxFrequency(nums = [1,4,8,13], k = 5)==2
assert Solution().maxFrequency(nums = [1,2,4], k = 5)==3
