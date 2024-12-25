#
# @lc app=leetcode.cn id=LCP 11 lang=python3
# @lcpr version=30204
#
# [LCP 11] 期望个数统计
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def expectNumber(self, scores: List[int]) -> int:
        return len(set(scores))
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

#

