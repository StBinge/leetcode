#
# @lc app=leetcode.cn id=2871 lang=python3
# @lcpr version=30204
#
# [2871] 将数组分割成最多数目的子数组
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        ret = 0
        cur = -1
        for n in nums:
            cur &= n
            if cur == 0:
                ret += 1
                cur = -1
        return max(1,ret)


# @lc code=end
assert Solution().maxSubarrays([0,8,0,0,0,23]) == 4
assert Solution().maxSubarrays([5,7,1,3]) == 1
assert Solution().maxSubarrays([1, 0, 2, 0, 1, 2]) == 3


#
# @lcpr case=start
# [1,0,2,0,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [5,7,1,3]\n
# @lcpr case=end

#
