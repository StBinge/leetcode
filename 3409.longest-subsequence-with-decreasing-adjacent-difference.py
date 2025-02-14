#
# @lc app=leetcode.cn id=3409 lang=python3
# @lcpr version=30204
#
# [3409] 最长相邻绝对差递减子序列
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        N = len(nums)
        mi, mx = min(nums), max(nums)
        mx_dif = mx - mi
        f = [[1] * (mx_dif + 1) for _ in range(N)]

        ret = 2
        for i in range(1, N):
            for j in range(i):
                dif = abs(nums[i] - nums[j])
                f[i][dif] = max(f[j][dif:]) + 1
            ret = max(ret, max(f[i]))
        return ret


# @lc code=end
assert Solution().longestSubsequence([5,8,9,8,6,1,7,4,7]) == 6
assert Solution().longestSubsequence([10,20,10,19,10,20]) == 5
assert Solution().longestSubsequence([6, 5, 3, 4, 2, 1]) == 4
assert Solution().longestSubsequence([16, 6, 3]) == 3


#
# @lcpr case=start
# [16,6,3]\n
# @lcpr case=end

# @lcpr case=start
# [6,5,3,4,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [10,20,10,19,10,20]\n
# @lcpr case=end

#
