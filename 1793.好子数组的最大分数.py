#
# @lc app=leetcode.cn id=1793 lang=python3
#
# [1793] 好子数组的最大分数
#
from sbw import *


# @lc code=start
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        left, right = k - 1, k + 1
        ret = nums[k]
        x = nums[k]
        while x:
            while left >= 0 and nums[left] >= x:
                left -= 1
            while right < N and nums[right] >= x:
                right += 1
            ret = max(ret, (right - left - 1) * x)
            x = max(nums[left] if left != -1 else 0, nums[right] if right != N else 0)
        return ret


# @lc code=end

assert Solution().maximumScore(nums=[5, 5, 4, 5, 4, 1, 1, 1], k=0) == 20
assert Solution().maximumScore(nums=[1, 4, 3, 7, 4, 5], k=3) == 15
