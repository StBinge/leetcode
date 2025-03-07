#
# @lc app=leetcode.cn id=2680 lang=python3
# @lcpr version=30204
#
# [2680] 最大或值
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        all_or=0
        multi=0
        for n in nums:
            multi|=all_or & n
            all_or|=n
        
        return max(((all_or^n) | n<<k | multi) for n in nums)


# @lc code=end
assert Solution().maximumOr([8, 1, 2], 2) == 35
assert Solution().maximumOr([12, 9], 1) == 30


#
# @lcpr case=start
# [12,9]\n1\n
# @lcpr case=end

# @lcpr case=start
# [8,1,2]\n2\n
# @lcpr case=end

#
