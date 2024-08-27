#
# @lc app=leetcode.cn id=1879 lang=python3
#
# [1879] 两个数组最小的异或值之和
#
from sbw import *


# @lc code=start
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        Mask = 1 << N
        f = [float("inf")] * Mask
        f[0] = 0
        for mask in range(1, Mask):
            c = mask.bit_count() - 1
            for i in range(N):
                if mask >> i & 1:
                    f[mask] = min(f[mask], f[mask ^ 1 << i] + (nums1[c] ^ nums2[i]))
        return f[-1]


# @lc code=end
assert Solution().minimumXORSum(nums1=[1, 0, 3], nums2=[5, 3, 4]) == 8
assert Solution().minimumXORSum(nums1=[1, 2], nums2=[2, 3]) == 2
