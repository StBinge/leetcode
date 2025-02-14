#
# @lc app=leetcode.cn id=3411 lang=python3
# @lcpr version=30204
#
# [3411] 最长乘积等价子数组
#
from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        # x 1 2 3 4 5 6 7 8 9 10
        # 1 0
        # 2 0 1
        # 3 0 0 1
        # 4 0 1 0 1
        # 5 0 0 0 0 1
        # 6 0 1 1 0 0 1
        # 7 0 0 0 0 0 0 1
        # 8 0 1 0 1 0 0 0 1
        # 9 0 0 1 0 0 0 0 0 1
        # 10 0 1 0 0 1 0 0 0 0 1
        masks = [
            0,
            0,
            0b10,
            0b100,
            0b1010,
            0b10000,
            0b100110,
            0b1000000,
            0b10001010,
            0b100000100,
            0b1000010010,
        ]
        left = 0
        ret = 2
        mask = 0
        for right, x in enumerate(nums):
            if mask & masks[x]:
                ret = max(ret, right - left)
                while mask & masks[x]:
                    mask ^= masks[nums[left]]
                    left += 1
            mask |= masks[x]

        return max(ret, len(nums) - left)


# @lc code=end
assert Solution().maxLength([1, 2, 3, 1, 4, 5, 1]) == 5
assert Solution().maxLength([2, 3, 4, 5, 6]) == 3
assert Solution().maxLength([1, 2, 1, 2, 1, 1, 1]) == 5


#
# @lcpr case=start
# [1,2,1,2,1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,4,5,1]\n
# @lcpr case=end

#
