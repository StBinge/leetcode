#
# @lc app=leetcode.cn id=2411 lang=python3
# @lcpr version=30204
#
# [2411] 按位或最大的最小子数组长度
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ret = [0] * N
        for i, x in enumerate(nums):
            ret[i] = 1
            for j in range(i - 1, -1, -1):
                if (nums[j] | x) == nums[j]:
                    break
                nums[j] |= x
                ret[j] = i - j + 1
        return ret


# @lc code=end
assert Solution().smallestSubarrays([1, 0]) == [1, 1]
assert Solution().smallestSubarrays([1, 2]) == [2, 1]
assert Solution().smallestSubarrays([1, 0, 2, 1, 3]) == [3, 3, 2, 2, 1]


#
# @lcpr case=start
# [1,0,2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#
