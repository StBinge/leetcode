#
# @lc app=leetcode.cn id=1588 lang=python3
#
# [1588] 所有奇数长度子数组的和
#
from sbw import *


# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ret = 0
        n = len(arr)
        for i in range(n):
            left_cnt = i
            left_even = (left_cnt + 1) // 2 + (left_cnt & 1 == 0)
            left_odd = left_cnt - left_even + 1
            right_cnt = n - i - 1
            right_even = (right_cnt + 1) // 2 + (right_cnt & 1 == 0)
            right_odd = right_cnt - right_even + 1
            cnt = left_even * right_even + left_odd * right_odd
            ret += cnt * arr[i]
        return ret


# @lc code=end
assert Solution().sumOddLengthSubarrays([10,11,12]) == 66
assert Solution().sumOddLengthSubarrays([1, 2]) == 3
assert Solution().sumOddLengthSubarrays([1, 4, 2, 5, 3]) == 58
