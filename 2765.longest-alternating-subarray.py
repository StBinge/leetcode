#
# @lc app=leetcode.cn id=2765 lang=python3
# @lcpr version=30204
#
# [2765] 最长交替子数组
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        idx = 0
        # nums.append(-1)
        mx = -1
        while idx < N - 1:
            if nums[idx] - nums[idx + 1] != -1:
                idx += 1
                continue
            cnt = 2
            while idx + 2 < N and nums[idx] == nums[idx + 2]:
                cnt += 1
                idx += 1
            mx = max(mx, cnt)
            idx += 1
        return mx


# @lc code=end
assert Solution().alternatingSubarray([2, 3, 4, 3, 4]) == 4
assert Solution().alternatingSubarray([14, 30, 29, 49, 3, 23, 44, 21, 26, 52]) == -1


#
# @lcpr case=start
# [2,3,4,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6]\n
# @lcpr case=end

#
