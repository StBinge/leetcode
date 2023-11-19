#
# @lc app=leetcode.cn id=330 lang=python3
#
# [330] 按要求补齐数组
#

from typing import List
# @lc code=start
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches=0
        idx,x=0,1
        N=len(nums)
        while x<=n:
            if idx<N and nums[idx]<=x:
                x+=nums[idx]
                idx+=1
            else:
                x*=2
                patches+=1
        return patches
            

# @lc code=end

assert Solution().minPatches([1,3],6)==1
assert Solution().minPatches([1,5,10],20)==2
assert Solution().minPatches([1,2,2],5)==0

