#
# @lc app=leetcode.cn id=396 lang=python3
#
# [396] 旋转函数
#
from typing import List
# @lc code=start
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        S,N=sum(nums),len(nums)
        f=sum(i*nums[i] for i in range(N))
        ret=f
        for i in range(1,N):
            f=f+S-N*nums[N-i]
            ret=max(ret,f)
        return ret
# @lc code=end

assert Solution().maxRotateFunction([4,3,2,6])==26
assert Solution().maxRotateFunction([100])==0