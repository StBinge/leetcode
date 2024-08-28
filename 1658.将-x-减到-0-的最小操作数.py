#
# @lc app=leetcode.cn id=1658 lang=python3
#
# [1658] 将 x 减到 0 的最小操作数
#
from sbw import *


# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        N = len(nums)
        left,right=0,0
        l_s,r_s=0,sum(nums)
        if r_s<x:
            return -1
        ret=N+1
        while left<N:
            while l_s+r_s>x and right<N:
                r_s-=nums[right]
                right+=1
            if l_s+r_s>x:
                break
            if l_s+r_s==x:
                ret=min(ret,N-right+left)
            l_s+=nums[left]
            left+=1
        return ret if ret<N+1 else -1


# @lc code=end

assert Solution().minOperations(nums=[1, 1, 4, 2, 3], x=5) == 2
assert Solution().minOperations(nums=[3, 2, 20, 1, 1, 3], x=10) == 5
assert Solution().minOperations(nums=[5, 6, 7, 8, 9], x=4) == -1
