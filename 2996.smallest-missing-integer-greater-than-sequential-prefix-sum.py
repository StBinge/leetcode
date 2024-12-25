#
# @lc app=leetcode.cn id=2996 lang=python3
# @lcpr version=30204
#
# [2996] 大于等于顺序前缀和的最小缺失整数
#
from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = nums[0]
        ss = set(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                s += nums[i]
            else:
                break

        while s in ss:
            s += 1
        return s


# @lc code=end
assert Solution().missingInteger([46, 8, 2, 4, 1, 4, 10, 2, 4, 10, 2, 5, 7, 3, 1]) == 47
assert Solution().missingInteger([38]) == 39
assert Solution().missingInteger([29, 30, 31, 32, 33, 34, 35, 36, 37]) == 297


#
# @lcpr case=start
# [1,2,3,2,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5,1,12,14,13]\n
# @lcpr case=end

#
