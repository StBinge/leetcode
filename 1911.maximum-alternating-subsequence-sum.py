#
# @lc app=leetcode.cn id=1911 lang=python3
# @lcpr version=30204
#
# [1911] 最大子序列交替和
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # [even_cnt,odd_cnt]
        f = [0, float("-inf")]

        for n in nums:
            f[0], f[1] = max(f[1] - n, f[0]), max(f[1], f[0] + n)
        return max(f)


# @lc code=end
assert Solution().maxAlternatingSum([6,2,1,2,4,5]) == 10
assert Solution().maxAlternatingSum([5, 6, 7, 8]) == 8
assert Solution().maxAlternatingSum([4, 2, 5, 3]) == 7


#
# @lcpr case=start
# [4,2,5,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,6,7,8]\n
# @lcpr case=end

# @lcpr case=start
# [6,2,1,2,4,5]\n
# @lcpr case=end

#
