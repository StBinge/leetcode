#
# @lc app=leetcode.cn id=2226 lang=python3
# @lcpr version=30204
#
# [2226] 每个小孩最多能分到多少糖果
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        left = 1
        right = max(candies)
        ret = 0
        while left <= right:
            mid = (left + right) >> 1
            cnt = sum(c // mid for c in candies)
            if cnt >= k:
                ret = mid
                left = mid + 1
            else:
                right = mid - 1
        return ret


# @lc code=end
assert Solution().maximumCandies(candies=[5, 8, 6], k=3) == 5


#
# @lcpr case=start
# [5,8,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,5]\n11\n
# @lcpr case=end

#
