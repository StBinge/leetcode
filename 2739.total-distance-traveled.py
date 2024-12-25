#
# @lc app=leetcode.cn id=2739 lang=python3
# @lcpr version=30204
#
# [2739] 总行驶距离
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        return (min((mainTank-1)//4,additionalTank)+mainTank)*10
# @lc code=end



#
# @lcpr case=start
# 5\n10\n
# @lcpr case=end

# @lcpr case=start
# 1\n2\n
# @lcpr case=end

#

