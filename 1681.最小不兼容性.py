#
# @lc app=leetcode.cn id=1681 lang=python3
#
# [1681] 最小不兼容性
#
from sbw import *


# @lc code=start
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        if max(Counter(nums).values()) > k:
            return -1

        N = len(nums)
        size = N // k
        nums.sort()

        @cache
        def dfs(left: int, pre):
            if left == 0:
                return 0
            if left.bit_count() % size == 0:
                lb = left & -left
                return dfs(left ^ lb, lb.bit_length() - 1)

            last = nums[pre]
            ret = 1000
            for i in range(pre + 1, N):
                if left & (1 << i) and last != nums[i]:
                    last = nums[i]
                    ret = min(ret, last - nums[pre] + dfs(left ^ (1 << i), i))
            return ret

        ret = dfs((1 << N) - 2, 0)
        return ret


# @lc code=end
assert Solution().minimumIncompatibility(nums=[5, 3, 3, 6, 3, 3], k=3) == -1
assert Solution().minimumIncompatibility(nums=[6, 3, 8, 1, 3, 1, 2, 2], k=4) == 6
assert Solution().minimumIncompatibility(nums=[1, 2, 1, 4], k=2) == 4
