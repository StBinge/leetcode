#
# @lc app=leetcode.cn id=3196 lang=python3
# @lcpr version=30204
#
# [3196] 最大化子数组的总成本
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        # f1 => single
        # f2 => pair
        f1,f2=float('-inf'),0
        # f = [[0, 0] for _ in range(N + 1)]
        for i, n in enumerate(nums):
            f1,f2=max(f1,f2)+n,f1-n
            # f[i + 1][0] = max(f[i]) + n
            # f[i + 1][1] = f[i][0] - n
        return max(f1,f2)


# @lc code=end
assert Solution().maximumTotalCost([-937]) == -937
assert Solution().maximumTotalCost([1, -1]) == 2
assert Solution().maximumTotalCost([0]) == 0
assert Solution().maximumTotalCost([1, -1, 1, -1]) == 4
assert Solution().maximumTotalCost([1, -2, 3, 4]) == 10


#
# @lcpr case=start
# [1,-2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,-1,1,-1]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

# @lcpr case=start
# [1,-1]\n
# @lcpr case=end

#
