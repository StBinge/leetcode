#
# @lc app=leetcode.cn id=1991 lang=python3
# @lcpr version=30204
#
# [1991] 找到数组的中间位置
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        left = 0
        for i, n in enumerate(nums):
            s -= n
            if left == s:
                return i
            left += n
        return -1


# @lc code=end
assert Solution().findMiddleIndex([1, -1, 4]) == 2
assert Solution().findMiddleIndex([2, 3, -1, 8, 4]) == 3


#
# @lcpr case=start
# [2,3,-1,8,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,-1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,5]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
