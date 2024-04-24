#
# @lc app=leetcode.cn id=3022 lang=python3
#
# [3022] 给定操作次数内使剩余元素的或值最小
#
from sbw import *

# @lc code=start
import heapq


class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        bits = max(nums).bit_length()
        mask = 0
        for b in range(bits - 1, -1, -1):
            mask |= 1 << b
            cur = -1
            cnt = 0
            for x in nums:
                cur &= mask & x
                if cur:
                    cnt += 1
                else:
                    cur = -1
                if cnt > k:
                    mask ^= 1 << b
                    break
        return ((1 << bits) - 1) ^ mask


# @lc code=end
assert Solution().minOrAfterOperations(nums = [10,7,10,3,9,14,9,4], k = 1) == 15
assert Solution().minOrAfterOperations(nums=[7, 3, 15, 14, 2, 8], k=4) == 2
assert Solution().minOrAfterOperations(nums=[3, 5, 3, 2, 7], k=2) == 3
