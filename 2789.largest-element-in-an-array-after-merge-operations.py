#
# @lc app=leetcode.cn id=2789 lang=python3
# @lcpr version=30204
#
# [2789] 合并后数组中的最大元素
#
from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        mx=0
        for i in range(len(nums)-1,-1,-1):
            n=nums[i]
            if mx>=n:
                mx+=n
            else:
                mx=n
        return mx



# @lc code=end
assert Solution().maxArrayValue([2,3,7,9,3])==21

#
# @lcpr case=start
# [2,3,7,9,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,3,3]\n
# @lcpr case=end

#
