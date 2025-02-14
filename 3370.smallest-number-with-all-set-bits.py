#
# @lc app=leetcode.cn id=3370 lang=python3
# @lcpr version=30204
#
# [3370] 仅含置位位的最小整数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def smallestNumber(self, n: int) -> int:
        bits=len(str(bin(n)))-2
        return (1<<bits)-1
# @lc code=end



#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

