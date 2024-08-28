#
# @lc app=leetcode.cn id=1787 lang=python3
#
# [1787] 使所有区间的异或结果为零
#
from sbw import *


# @lc code=start
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        Max = 1<<(max(nums).bit_length())
        N = len(nums)
        f0 = [0] * Max
        f1 = [float("inf")] * Max
        g = [float("inf")] * k

        for i in range(k):
            cnt = defaultdict(int)
            col_tot = 0
            for j in range(i, N, k):
                cnt[nums[j]] += 1
                col_tot += 1
            if i == 0:
                for xor in range(Max):
                    # f0[xor]=min(f0[xor],col_tot-cnt[xor])
                    f0[xor] = col_tot - cnt[xor]
                    g[0] = min(g[0], f0[xor])
            else:
                for xor in range(Max):
                    f1[xor] = g[i - 1] + col_tot
                    for x in cnt:
                        f1[xor] = min(f1[xor], f0[xor ^ x] + col_tot - cnt.get(x))
                    g[i] = min(g[i], f1[xor])
                f0, f1 = f1, f0
        return f0[0]


# @lc code=end
assert Solution().minChanges(nums=[1, 2, 4, 1, 2, 5, 1, 2, 6], k=3) == 3
assert Solution().minChanges(nums=[3, 4, 5, 2, 1, 7, 3, 4, 7], k=3) == 3
assert Solution().minChanges(nums=[1, 2, 0, 3, 0], k=1) == 3
