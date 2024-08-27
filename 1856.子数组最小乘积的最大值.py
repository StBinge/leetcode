#
# @lc app=leetcode.cn id=1856 lang=python3
#
# [1856] 子数组最小乘积的最大值
#
from sbw import *


# @lc code=start
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        N = len(nums)
        presums = list(accumulate(nums, initial=0))
        Mod = 10**9 + 7
        left = [-1] * N
        right = [N] * N
        st = []
        for i, n in enumerate(nums):
            while st and nums[st[-1]] >= n:
                idx = st.pop()
                right[idx] = i
            if st:
                left[i] = st[-1]
            st.append(i)
        ret = 0
        for i, n in enumerate(nums):
            ret = max(ret, n * (presums[right[i]]-presums[left[i]+1]))
        return ret % Mod


# @lc code=end
assert Solution().maxSumMinProduct([3, 1, 5, 6, 4, 2]) == 60
assert Solution().maxSumMinProduct([1, 1, 3, 2, 2, 2, 1, 5, 1, 5]) == 25
assert Solution().maxSumMinProduct([2, 3, 3, 1, 2]) == 18
assert Solution().maxSumMinProduct([1, 2, 3, 2]) == 14
