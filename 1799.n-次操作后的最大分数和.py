#
# @lc app=leetcode.cn id=1799 lang=python3
#
# [1799] N 次操作后的最大分数和
#
from sbw import *


# @lc code=start
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        N = len(nums)
        nums.reverse()
        gcds = [[0] * N for _ in range(N)]

        for i in range(N):
            for j in range(i + 1, N):
                g = math.gcd(nums[i], nums[j])
                gcds[i][j] = g
                gcds[j][i] = g

        MASK = 1 << N
        f = [0] * MASK

        for j in range(1, MASK):
            bits = j.bit_count()
            if bits % 2:
                continue
            for x in range(N):
                if j & (1 << x) == 0:
                    continue
                m = 1 << x
                for y in range(x + 1, N):
                    if j & (1 << y):
                        _m = m | (1 << y)
                        f[j] = max(
                            f[j], 
                            f[j ^ _m] + gcds[x][y] * bits // 2
                        )
        return f[-1]


# @lc code=end
assert Solution().maxScore([3, 4, 6, 8]) == 11
assert Solution().maxScore([1, 2, 3, 4, 5, 6]) == 14
assert Solution().maxScore([1, 2]) == 1
