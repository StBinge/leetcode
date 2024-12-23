#
# @lc app=leetcode.cn id=2413 lang=python3
# @lcpr version=30204
#
# [2413] 最小偶倍数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            return n
        return n*2
# @lc code=end



#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 6\n
# @lcpr case=end

#

