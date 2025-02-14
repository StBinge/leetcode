#
# @lc app=leetcode.cn id=2905 lang=python3
# @lcpr version=30204
#
# [2905] 找出满足差值条件的下标 II
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findIndices(
        self, nums: List[int], indexDifference: int, valueDifference: int
    ) -> List[int]:
        N = len(nums)
        if N - 1 < indexDifference:
            return [-1, -1]
        mi = mx = 0

        for i in range(indexDifference, len(nums)):
            pre = i - indexDifference
            if nums[pre] < nums[mi]:
                mi = pre
            if nums[pre] > nums[mx]:
                mx = pre
            if abs(nums[mi] - nums[i]) >= valueDifference:
                return [mi, i]
            if abs(nums[mx] - nums[i]) >= valueDifference:
                return [mx, i]
        return [-1, -1]


# @lc code=end
assert Solution().findIndices(nums=[1, 2, 3], indexDifference=2, valueDifference=4) == [
    -1,
    -1,
]
assert Solution().findIndices(nums=[2, 1], indexDifference=0, valueDifference=0) == [
    0,
    0,
]
assert Solution().findIndices(
    nums=[5, 1, 4, 1], indexDifference=2, valueDifference=4
) == [0, 3]


#
# @lcpr case=start
# [5,1,4,1]\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n0\n0\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n2\n4\n
# @lcpr case=end

#
