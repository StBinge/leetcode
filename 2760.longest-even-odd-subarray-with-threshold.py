#
# @lc app=leetcode.cn id=2760 lang=python3
# @lcpr version=30204
#
# [2760] 最长奇偶子数组
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ret = 0
        idx = 0
        N = len(nums)
        while idx < N:
            while idx < N and (nums[idx] > threshold or nums[idx] & 1 == 1):
                idx += 1
            if idx == N:
                break
            l = idx
            idx += 1
            while (
                idx < N
                and nums[idx] <= threshold
                and nums[idx] & 1 != nums[idx - 1] & 1
            ):
                idx += 1
            ret = max(ret, idx - l)
        return ret


# @lc code=end
assert Solution().longestAlternatingSubarray([4], 1) == 0
assert Solution().longestAlternatingSubarray([1], 1) == 0
assert Solution().longestAlternatingSubarray([3, 2, 5, 4], 5) == 3

#
# @lcpr case=start
# [3,2,5,4]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4,5]\n4\n
# @lcpr case=end

#
